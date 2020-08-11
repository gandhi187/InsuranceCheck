from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class InsuranceCheck(FormAction):

    def name(self):
        return "insurance_check"
    
    @staticmethod
    def required_slots(tracker) -> List[Text]:  
        print (tracker.get_slot('age'))
        print (tracker.get_slot('profession'))

        # if tracker.get_slot('age') is None: 
        #     print ("none", tracker.get_slot('age'))

        # if tracker.get_slot('age') is None:
        #     print ("none", tracker.get_slot('age'))
        #     return ["age"]
        # elif  (int) (tracker.get_slot('age')) >= 18:
        #     return ["profession"]
        # else: 
        return ["age","profession","familyStatus","living","ownership","leisure"]
     

    # def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

    #     return {
    #         "age":[
    #             self.from_intent(intent="inform")
    #         ]
    #     }

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

        dispatcher.utter_message("Thanks, great job!")
        return []   