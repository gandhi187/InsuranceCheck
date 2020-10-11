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

## Kath
* product
    - action_moreInfo_buttons
    - action_reset_productslot

## Secret
* katharina
 - utter_response_katha1
* affirm
 - utter_response_katha2
* metoo
 - utter_response_katha3
* deny
 - utter_goodbye

## Secret2
* denizabi
 - utter_answer_deniz

## GeneratedStory1

* greet
    - utter_greet
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* question
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"destination"}
* destination{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* question
    - slot{"destination":"Indien"}
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_months{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - slot{"travel_days":"4"}
    - insurance_check
    - slot{"travel_days":120}
    - slot{"requested_slot":"moreTravel"}
* question
    - slot{"destination":"Indien"}
    - slot{"travel_days":"4"}
    - utter_explain_whyMoreTravel
    - insurance_check
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"niedrig"}
    - slot{"luggage":"niedrig"}
    - slot{"luggage":"niedrig"}
    - insurance_check
    - slot{"luggage":"niedrig"}
    - slot{"requested_slot":"financeLoss"}
* question
    - slot{"destination":"Indien"}
    - slot{"travel_days":"4"}
    - slot{"luggage":"niedrig"}
    - utter_explain_whyFinanceLoss
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
    - slot{"destination":"Indien"}
    - slot{"travel_days":"4"}
    - slot{"luggage":"niedrig"}
    - slot{"financeLoss":"mittel"}
* inform{"age":"1977"}
    - slot{"age":"1977"}
    - insurance_check
    - slot{"age":43}
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Asien"}
