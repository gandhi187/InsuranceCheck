
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

