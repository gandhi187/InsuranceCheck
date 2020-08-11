
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

## explain_age
> check_affirm
  - slot{"requested_slot":"age"}
* question
  - utter_explain_age
  - insurance_check
  - form{"name": null}
  - utter_slot_values

  
## check_stop
> check_affirm
* out_of_scope
  - utter_ask_continue
* deny
    - action_deactivate_form
    - form{"name": null}
    - utter_goodbye

## check_continue
> check_affirm
* out_of_scope
  - utter_ask_continue
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_goodbye

## no_check
* greet
  - utter_greet
* deny
  - utter_goodbye