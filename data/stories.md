## user_affirm_check
* greet
  - utter_greet
* affirm
  - insurance_check
  - form{"name": "insurance_check"}
> check_affirm

## happy_path
> check_affirm
  - form{"name": null}
  - action_fetch_continent
  - utter_slot_values
  - utter_goodbye

## check_stop
> check_affirm
* out_of_scope   
  - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye

## ask_whats_possible
* whatsPossible
  - utter_explain_whatspossible

## check_continue
> check_affirm
* out_of_scope
  - utter_ask_continue
* affirm
  - insurance_check
  - form{"name": null}
  - action_fetch_continent
  - utter_slot_values
  - utter_goodbye

## ask_insurance
* query_knowledge_base
  - action_query_knowledge_base

## no_check
* greet
  - utter_greet
* deny
  - utter_goodbye

## travel_warning
* travelWarning
 - action_fetch_travel_warning

## corona
* corona 
 - action_fetch_corona

## Generated Story1

* greet
    - utter_greet
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* destination{"destination":"Mexiko"}
    - slot{"destination":"Mexiko"}
    - slot{"destination":"Mexiko"}
    - insurance_check
    - slot{"destination":"Mexiko"}
    - slot{"requested_slot":"travel_days"}
* travel_days{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - insurance_check
    - slot{"travel_days":"4"}
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"hoch"}
    - slot{"luggage":"hoch"}
    - slot{"luggage":"hoch"}
    - insurance_check
    - slot{"luggage":"hoch"}
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"hoch"}
    - slot{"financeLoss":"hoch"}
    - slot{"financeLoss":"hoch"}
    - insurance_check
    - slot{"financeLoss":"hoch"}
    - slot{"requested_slot":"occasion"}
* deny
    - insurance_check
    - slot{"occasion":false}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Nordamerika"}
    - utter_slot_values
    - slot{"destination":"Mexiko"}
    - slot{"travel_days":"4"}
    - slot{"luggage":"hoch"}
    - slot{"financeLoss":"hoch"}
    - utter_goodbye

## New Story

* greet
    - utter_greet
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* destination{"destination":"Mexiko"}
    - slot{"destination":"Mexiko"}
    - insurance_check
    - slot{"destination":"Mexiko"}
    - slot{"requested_slot":"travel_days"}
* travel_days{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - insurance_check
    - slot{"travel_days":"4"}
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"hoch"}
    - slot{"financeLoss":"hoch"}
    - insurance_check
    - slot{"financeLoss":"hoch"}
    - slot{"requested_slot":"occasion"}
* deny
    - insurance_check
    - slot{"occasion":false}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Nordamerika"}
    - utter_slot_values
    - utter_goodbye
* insult
    - utter_respond_insult
* corona
    - action_fetch_corona
    - slot{"coronaCases":113954}
* query_knowledge_base{"object_type":"Auslandsreisekrankenversicherung"}
    - slot{"object_type":"Auslandsreisekrankenversicherung"}
    - action_query_knowledge_base
    - slot{"object_type":"Auslandsreisekrankenversicherung"}
    - slot{"mention":null}
    - slot{"attribute":null}
    - slot{"knowledge_base_last_object":null}
    - slot{"knowledge_base_last_object_type":"Auslandsreisekrankenversicherung"}
    - slot{"knowledge_base_listed_objects":[5,0,3,1,4]}

## New Story

* greet
    - utter_greet
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* question
    - utter_explain_whyDestination
    - utter_ask_continue
* affirm
    - insurance_check
    - slot{"requested_slot":"destination"}
* destination{"destination":"Mexiko"}
    - slot{"destination":"Mexiko"}
    - slot{"destination":"Mexiko"}
    - insurance_check
    - slot{"destination":"Mexiko"}
    - slot{"requested_slot":"travel_days"}
* question
    - slot{"destination":"Mexiko"}
    - utter_explain_whyTravelDays
    - slot{"destination":"Mexiko"}
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - insurance_check
    - slot{"travel_days":"4"}
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"niedrig"}
    - slot{"financeLoss":"niedrig"}
    - insurance_check
    - slot{"financeLoss":"niedrig"}
    - slot{"requested_slot":"occasion"}
* deny
    - insurance_check
    - slot{"occasion":false}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Nordamerika"}
    - utter_slot_values
    - utter_goodbye

## interactive_story_1
* affirm
    - insurance_check
    - form{"name": "insurance_check"}
    - slot{"requested_slot": "destination"}
* dontKnow
    - action_fetch_continent
    - action_listen
    - slot{"destination": "Null"}
    - insurance_check
    - slot{"requested_slot": "continent"}

## changeDestination 
* changeDestination
    - action_reset_destination
    - insurance_check
    - form{"name": "insurance_check"}
    - form{"name": null}
    - action_fetch_continent
    - utter_slot_values
