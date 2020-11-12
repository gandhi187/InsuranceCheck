from typing import Any, Text, Dict, List, Union
from datetime import date
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from .validateCountry import *
from .buildRecommendation import *
from rasa_sdk.events import SlotSet
from .MyKnowledgeBase import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk.knowledge_base import *
from rasa_sdk.events import Restarted
from rasa_sdk import utils
import requests


class InsuranceCheck(FormAction):

    def name(self):
        return "insurance_check"

    @staticmethod
    def required_slots(tracker) -> List[Text]:

        # if tracker.get_slot('age') is None:
        #     print ("none", tracker.get_slot('age'))

        if tracker.get_slot('destination') == 'Null':
            if tracker.get_slot('travel_days') is None:
                print ("none", tracker.get_slot('travel_days'))
                return ["continent", "travel_days", "occasionDetails", "moreTravel", "age", "group"]
            elif (int)(tracker.get_slot('travel_days')) <= 45:
                print("Reisegepäck")
                return ["continent", "travel_days", "luggage", "financeLoss", "moreTravel", "age", "group"]
            elif (int)(tracker.get_slot('travel_days')) >= 45:
                return ["continent", "travel_days", "moreTravel", "age", "group"]
        else:
            if tracker.get_slot('travel_days') is None:
                print ("none", tracker.get_slot('travel_days'))
                return ["destination", "travel_days", "moreTravel", "age", "group"]
            elif (int)(tracker.get_slot('travel_days')) <= 45:
                print("Reisegepäck")
                return ["destination", "travel_days", "luggage", "financeLoss", "moreTravel", "age", "group"]
            elif (int)(tracker.get_slot('travel_days')) >= 45:
                return ["destination", "travel_days", "moreTravel", "age", "group"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        #print(self.get_entity_value("travel_days"))
        #print(tracker.latest_message['entities'][0]['value'])

        return {

            "travel_days": [
                self.from_entity(entity="duration", intent="travel_days")
            ],

            "group": [
                self.from_intent(intent="affirm", value=True),
                self.from_intent(intent="deny", value=False),
            ],

            "occasion": [
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

        unit = tracker.latest_message['entities'][0]['additional_info']['unit']
        print(unit)
        print (value)
        oldValue = value
        newValue = self.calculateDays(value, unit)
        print ("new Value " + str(newValue))

        if int(newValue) < 5:
            dispatcher.utter_message(
                "Bei " + str(newValue) + " Tagen , wirst du wohl mit Hangepäck  nach " + destination + " reisen")
            return {"travel_days": newValue}
        elif int(newValue) > 5:
            dispatcher.utter_message(
                "Bei " + str(newValue) + " Tagen, wirst du wohl mit größerem Gepäck nach " + destination + " reisen")
            return {"travel_days": newValue}
        else:
            return {"travel_days": None}

    def validate_destination(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        if value is None:
            return {"destination": "Null"}
        if (value == 'Deutschland' or value == "deutschland"):
            dispatcher.utter_message(template="utter_noInsuranceCover")
            return None
        print("destination: " + value)
        countryCode = FindCountryCode(value)
        print(countryCode)
        continent = GetContinentFromCountry(countryCode)
        print(continent)

        if (continent == "Europa"):
            dispatcher.utter_message(
                template="utter_answerDestination_insideEurope")
            return {"destination": value}
        else:
            dispatcher.utter_message(
                template="utter_answerDestination_outsideEurope")
            return {"destination": value}

    def validate_age(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        a = date.today()
        ageCalculated = a.year - int(value)

        if ageCalculated < 18:
            dispatcher.utter_message(template="utter_tooYoung")
            return None
        if ageCalculated > 125:
            dispatcher.utter_message(
                "Respekt, dass du in diesem Alter noch auf Reisen gehst, jedoch kann ich dir keine passende Versicherung vorschlagen")
            return None
        else:
            return {"age": ageCalculated}

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
        #occasionDetails = tracker.get_slot('occasionDetails')
        moreTravel = tracker.get_slot("moreTravel")
        age = tracker.get_slot("age")
        group = tracker.get_slot("group")

        jsonCarousel = queryDB(
            travel_days, luggage, financeLoss, moreTravel, age, group, destination)
       # jsonCarousel2= {"type": "template", "payload": {"template_type": "generic", "elements": [{"title": "Auslandsversicherung Langzeit ab 35 Jahre", "subtitle": "blabalba", "image_url": "https://i.imgur.com/EXp0PV6.png", "buttons": [{"title": "Mehr", "url": "http://link.url", "type": "web_url"}, {"title": "postback name", "type": "postback", "payload": "/greet"}]}]}}
        print(jsonCarousel)
        dispatcher.utter_message("Deine Vorschläge")
        dispatcher.utter_message(attachment=jsonCarousel)
        self.tag_convo(tracker, '[{"value":"Till Submit","color":"e5ff00"}]')
        dispatcher.utter_message("Ich hoffe ich konnte dir weiterhelfen :) auf deiner Reise nach : " +
                                 destination + ". Klicke auf  'Mehr', um weitere Informationen über das gewünschte Produkt zu erhalten")
        dispatcher.utter_message(
            "Du kannst dich auch nach der aktuellen Corona-Lage in deinem Zielland: " + destination + " bei mir erkundigen")
        return []

    def calculateDays(self, value, formatType):
        print ("calculate " + str(value) + " format :" + formatType)
        intValue = int(value)
        if formatType == "day":
            print (value)
            return intValue
        elif formatType == "week":
            print ("travel_weeks")
            print (intValue*7)
            return intValue*7
        elif formatType == "month":
            print (intValue*30)
            return intValue*30
        elif formatType == "year":
            print (intValue*365)
            return intValue*365

    def tag_convo(self, tracker: Tracker, label: Text) -> None:
        endpoint = f"https://admin.dave-chatbot.de/api/conversations/{tracker.sender_id}/tags"
        requests.post(url=endpoint, data=label)
        return


class FetchContinentAction(Action):
    def name(self):
        return "action_fetch_continent"

    def run(self, dispatcher, tracker, domain):
        data = tracker.get_slot("destination")
        if data is None or data == "Null":
            return [SlotSet("destination", "Null")]
        else:
            countryCode = FindCountryCode(data)
            continent = GetContinentFromCountry(countryCode)
            return [SlotSet("continent", continent)]


class FetchCoronaAction(Action):
    def name(self):
        return "action_fetch_corona"

    def run(self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        #countryCode = FindCountryCode(destination)
        data = getCoronaInformation(destination)
        activeCases = data['active']
        deaths = data['deaths']
        #deaths = data['countrydata'][0]['total_serious_cases']
        #dangerRank = data['countrydata'][0]['total_danger_rank']

        dispatcher.utter_message("In " + destination + " gibt es derzeit " + str(activeCases) +
                                 " aktive Corona Fälle. \n Seit Ausbruch gab es " + str(deaths) + " Todesfälle.")

        return [SlotSet("coronaCases", activeCases)]


class FetchTravelWarning(Action):
    def name(self):
        return "action_fetch_travel_warning"

    def run(self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        data = getTravelWarning(destination)
        travelWarningText = data['data']['lang']['de']['advice']
        print(travelWarningText)
        travelWarningRating = data['data']['situation']['rating']
        print (travelWarningRating)

        dispatcher.utter_message("In " + destination + " lautet die Reisewarnung: " +
                                 travelWarningText + " \n Reisewarnung-Stufe " + str(travelWarningRating) + " von 5")

        return [SlotSet("travelWarning", travelWarningRating)]


class ResetDestination(Action):
    def name(self):
        return "action_reset_destination"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("destination", None)]


class ResetTraveldays(Action):
    def name(self):
        return "action_reset_travel_days"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("travel_days", None)]


"""
Custom Actions to query the Knowledge-Base (JSON-Object)

"""


class MyKnowledgeBaseAction(ActionQueryKnowledgeBase):
    def __init__(self):
        json = getJsonData()

        #knowledge_base = InMemoryKnowledgeBase(response)
        knowledge_base = InMemoryKnowledgeBase(json)

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


class ActionRestartBot(Action):

    def name(self) -> Text:

        return "action_restart_bot"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_ask_restart")

        return [Restarted()]


class FetchActionButtons(Action):

    def name(self) -> Text:

        return "action_moreInfo_buttons"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.get_slot("product")
        print("Product " + product)
        buttons = [{"title": "Weitere Informationen", "payload": "Was ist versichert in " +
                    product}, {"title": "Aktuelle Corona Lage", "payload": "Corona Situation"}]
        dispatcher.utter_button_message("Was möchtest du erfahren ?", buttons)

        return []


class ResetProductSlot(Action):

    def name(self) -> Text:

        return "action_reset_productslot"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [SlotSet("product", None)]


class ResponseInsult(Action):

    def name(self) -> Text:

        return "action_response_insult"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        link = getRandomDogImage()
        dispatcher.utter_message(
            text="Das war gemein :( Vll. heitert dich ja das auf :")
        dispatcher.utter_message(image=link)
        return []


class WeatherUpdate(Action):

    def name(self) -> Text:

        return "action_response_weather"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,

            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            destination = tracker.get_slot('destination')
            # Hier die API-Abfrage
            temperature = getWeather(destination)
            # Hier die Antwort
            dispatcher.utter_message(
            text=   " Die Temperatur beträgt " + str(temperature) + " in deinem Reiseland " + destination)

            return []
