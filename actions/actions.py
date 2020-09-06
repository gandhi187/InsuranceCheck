from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from .validateCountry import *
from rasa_sdk.events import SlotSet
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase

class InsuranceCheck(FormAction):

    def name(self):
        return "insurance_check"
    
    @staticmethod
    def required_slots(tracker) -> List[Text]:  
       
        # if tracker.get_slot('age') is None: 
        #     print ("none", tracker.get_slot('age'))

        if tracker.get_slot('travel_days') is None:
            print ("none", tracker.get_slot('travel_days'))
            return ["destination", "travel_days"]
        elif  (int) (tracker.get_slot('travel_days')) <= 30:
            print("Reisegepäck")
            return ["destination", "travel_days","luggage","financeLoss"]
        elif (int) (tracker.get_slot('travel_days')) >= 30: 
            return ["destination", "travel_days"]
     

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

    #     return {
    #         "age":[
    #             self.from_intent(intent="inform")
    #         ]
    #     }


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
        
        dispatcher.utter_message("In " + destination + " lautet die Reisewarnung: " + travelWarningRating + " \n Reisewarnung-Stufe " + str(travelWarningRating) + " von 5")

        return [SlotSet("travelWarning",travelWarningRating)]

class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        knowledge_base = InMemoryKnowledgeBase("data/knowledgebase.json")
        super().__init__(knowledge_base)