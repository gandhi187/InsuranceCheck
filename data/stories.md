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

## New Story_5

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

## New Story_4

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

## New Story_3

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

## New Story_2

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* destination{"destination":"Türkei"}
    - slot{"destination":"Türkei"}
    - slot{"destination":"Türkei"}
    - insurance_check
    - slot{"destination":"Türkei"}
    - slot{"requested_slot":"travel_days"}
* travel_months{"travel_days":"8"}
    - slot{"travel_days":"8"}
    - slot{"travel_days":"8"}
    - insurance_check
    - slot{"travel_days":240}
    - slot{"requested_slot":"occasionDetails"}
* occasionDetails{"occasionDetails":"Urlaub"}
    - slot{"occasionDetails":"Urlaub"}
    - slot{"occasionDetails":"Urlaub"}
    - insurance_check
    - slot{"occasionDetails":"Urlaub"}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* inform{"age":"1988"}
    - slot{"age":"1988"}
    - slot{"age":"1988"}
    - insurance_check
    - slot{"age":32}
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Asien"}
    - utter_slot_values
    - utter_goodbye
* changeDestination
    - slot{"destination":"Türkei"}
    - slot{"travel_days":"8"}
    - slot{"occasionDetails":"Urlaub"}
    - slot{"age":"1988"}
    - action_reset_destination
    - slot{"destination":null}
    - insurance_check
    - utter_ask_destination
* destination{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - action_fetch_continent
    - slot{"continent":"Asien"}
    - utter_slot_values
    - utter_goodbye

## Change Destination 
* changeDestination
    - slot{"destination":"Türkei"}
    - slot{"travel_days":"8"}
    - slot{"occasionDetails":"Urlaub"}
    - slot{"age":"1988"}
    - action_reset_destination
    - action_reset_travel_days
    - slot{"destination":null}
    - slot {"destination":null}
    - insurance_check
    - utter_ask_destination
* destination{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* travel_months{"travel_days":"8"}
    - slot{"travel_days":"8"}
    - insurance_check
    - slot{"travel_days":240}
    - insurance_check
    - action_fetch_continent
    - slot{"continent":"Asien"}
    - utter_slot_values
    - utter_goodbye

## Kath
* product
    - utter_whats_covered

## Generated Story 1

* query_knowledge_base{"object_type":"Auslandsreisekrankenversicherung"}
    - slot{"object_type":"Auslandsreisekrankenversicherung"}
    - action_query_knowledge_base
    - slot{"object_type":"Auslandsreisekrankenversicherung"}
    - slot{"mention":null}
    - slot{"attribute":null}
    - slot{"knowledge_base_last_object":null}
    - slot{"knowledge_base_last_object_type":"Auslandsreisekrankenversicherung"}
    - slot{"knowledge_base_listed_objects":[0,2,4,5,3]}

## Secret
* katharina
 - utter_response_katharina1
* affirm
 - utter_response_katharina2
* metoo
 - utter_response_katharina3
* deny
 - utter_goodbye
