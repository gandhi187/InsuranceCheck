from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from .validateCountry import *
from rasa_sdk.events import SlotSet
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.knowledge_base import *
from rasa_sdk import utils

class InsuranceCheck(FormAction):

    def name(self):
        return "insurance_check"
    
    @staticmethod
    def required_slots(tracker) -> List[Text]:  
       
        # if tracker.get_slot('age') is None: 
        #     print ("none", tracker.get_slot('age'))

        if tracker.get_slot('travel_days') is None:
            print ("none", tracker.get_slot('travel_days'))
            return ["destination", "travel_days","occasion","moreTravel"]
        elif  (int) (tracker.get_slot('travel_days')) <= 30:
            print("Reisegepäck")
            return ["destination", "travel_days","luggage","financeLoss","occasion","moreTravel"]
        elif (int) (tracker.get_slot('travel_days')) >= 30: 
            return ["destination", "travel_days","occasion","moreTravel"]
     

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
            
            "occasion":[
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),

            ],
            "moreTravel": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ]
                }


    def validate_travel_days(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        destination = tracker.get_slot("destination")

        if int(value)<5:
            dispatcher.utter_message("Bei " + str(value) +  " Tagen, wirst du wohl mit Hangepäck  nach " + destination + " reisen")
            return {"travel_days":value}
        elif int(value)>5:
            dispatcher.utter_message("Bei " + str(value) + " Tagen, wirst du wohl mit größerem Gepäck nach " + destination + " reisen")
            return {"travel_days":value}
        else:
            return {"travel_days":None}


    def validate_destination(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print(value)
        countryCode = FindCountryCode(value)
        print(countryCode)
        continent = GetContinentFromCountry(countryCode)
        print(continent)
        if (continent == "Europa"):
            dispatcher.utter_message(template="utter_answerDestination_insideEurope")
            return {"destination":value}
        else:
            dispatcher.utter_message(template="utter_answerDestination_outsideEurope")
            return {"destination":value}


    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        if int(value)<18:
            dispatcher.utter_message(template="utter_tooYoung")
            return self.deactivate()
        if int(value)>125:
            dispatcher.utter_message("unnmöglich")
            return self.deactivate()
        else:
            dispatcher.utter_message("Über 18 ")
            return {"age": value} 

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        destination = tracker.get_slot('destination')
        continent = tracker.get_slot('continent')
        travel_days = tracker.get_slot('travel_days')
        luggage = tracker.get_slot('luggage')
        financeLoss = tracker.get_slot('financeLoss')
        occasion = tracker.get_slot('occasion')
        moreTravel = tracker.get_slot("moreTravel")

        if (int(travel_days) <= 30 and moreTravel == False and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' ):
            print ('Empfehlung 1')
            dispatcher.utter_message("Empfehlung für deine Reise nach " + destination + " Einmalige Reisekrankenversicherung \n Reisgepäckversicherung \n Reiserücktrittversicherung")
        elif (int(travel_days) <= 30 and moreTravel == False and luggage == 'niedrig' and financeLoss == 'niedrig' ):
            print ('Empfehlung 2')
            dispatcher.utter_message("Empfehlung für deine Reise nach " + destination + " Einmalige Reisekrankenversicherung")
        elif (int(travel_days) <= 30 and moreTravel == True and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' ):
            dispatcher.utter_message("Empfehlung für deine Reise nach " + destination + " Jahres-Reisekrankenversicherung \n Reisgepäckversicherung \n Reiserücktrittversicherung")
        elif (int(travel_days) <= 30 and moreTravel == True and luggage == 'niedrig' and financeLoss == 'niedrig' ):
            dispatcher.utter_message("Empfehlung für deine Reise nach " + destination + " Jahres-Reisekrankenversicherung ")
        elif (int(travel_days) >= 30 ) : 
            dispatcher.utter_message("Empfehlung für deine Reise nach " + destination + " Da du für + " + int (travel_days) + " verreist, .... COMING SOON ")

        return []   


class FetchContinentAction(Action):
    def name(self):
        return "action_fetch_continent"

    def run(self, dispatcher, tracker, domain):
        data = tracker.get_slot("destination")
        countryCode = FindCountryCode(data)
        continent = GetContinentFromCountry(countryCode)

        return [SlotSet("continent", continent)]  

class FetchCoronaAction(Action):
    def name (self):
        return "action_fetch_corona"

    def run (self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        #countryCode = FindCountryCode(destination)
        data = getCoronaInformation(destination)
        activeCases = data['countrydata'][0]['total_active_cases']
        seriousCases = data['countrydata'][0]['total_serious_cases']
        totalCases = activeCases+seriousCases
        dangerRank = data['countrydata'][0]['total_danger_rank']
        
        dispatcher.utter_message("In " + destination + " gibt es derzeit " + str(totalCases) + " aktive Corona Fälle. \n Das Land befindet sich auf Rang " + str(dangerRank) )

        return [SlotSet("coronaCases",totalCases)]

class FetchTravelWarning(Action):
    def name (self):
        return "action_fetch_travel_warning"
    def run (self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        data = getTravelWarning(destination)
        travelWarningText = data['data']['lang']['de']['advice']
        print(travelWarningText)
        travelWarningRating = data['data']['situation']['rating']
        print (travelWarningRating)
        
        dispatcher.utter_message("In " + destination + " lautet die Reisewarnung: " + travelWarningText + " \n Reisewarnung-Stufe " + str(travelWarningRating) + " von 5")

        return [SlotSet("travelWarning",travelWarningRating)]


"""
Custom Actions to query the Knowledge-Base (JSON-Object)

"""
class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("actions/knowledgebase.json")
        super().__init__(knowledge_base)



    async def utter_objects(
        self,
        dispatcher: CollectingDispatcher,
        object_type: Text,
        objects: List[Dict[Text, Any]],
    ) -> None:
        """
        Utters a response to the user that lists all found objects.

        Args:
            dispatcher: the dispatcher
            object_type: the object type
            objects: the list of objects
        """
        if objects:
            dispatcher.utter_message(
                text=f"Folgendes ist in der '{object_type}' versichert:"
            )

            if utils.is_coroutine_action(
                self.knowledge_base.get_representation_function_of_object
            ):
                repr_function = await self.knowledge_base.get_representation_function_of_object(
                    object_type
                )
            else:
                repr_function = self.knowledge_base.get_representation_function_of_object(
                    object_type
                )

            for i, obj in enumerate(objects, 1):
                dispatcher.utter_message(text=f"{i}: {repr_function(obj)}")
        else:
            dispatcher.utter_message(
                text=f"Ich konnte leider nichts zu  '{object_type}' finden."
            )

    def utter_attribute_value(
        self,
        dispatcher: CollectingDispatcher,
        object_name: Text,
        attribute_name: Text,
        attribute_value: Text,
    ) -> None:
        """
        Utters a response that informs the user about the attribute value of the
        attribute of interest.

        Args:
            dispatcher: the dispatcher
            object_name: the name of the object
            attribute_name: the name of the attribute
            attribute_value: the value of the attribute
        """
        if attribute_value:
            dispatcher.utter_message(
                text=f" Für '{object_name}' ist '{attribute_value}'  '{attribute_name}' ."
            )
        else:
            dispatcher.utter_message(
                text=f"Leider konnte ich unter dem Schlagwort '{attribute_name}' zu '{object_name}' nichts finden."
            )

