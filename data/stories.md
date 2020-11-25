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

## no_check
* greet
  - utter_greet
* deny
  - utter_goodbye

## travel_warning
* travelWarning
 - action_fetch_travel_warning
 - action_RKIWarning

## Music
* play_music
 - utter_play_music

## Kath
* product
    - action_moreInfo_buttons
    - action_reset_productslot

## changeDestination
* changeDestination
- action_reset_destination

## changeTravelDays
* changeTravelDays
- action_reset_travel_days

## happy
* happy
 - utter_answer_happy

## explainBackground
* provocate
 - utter_response_provocate
 - utter_response_provocate2
* whatsPossible
 - utter_explain_whatspossible
* researchquestion
 - utter_response_research_question
 - utter_response_research_question2
 - utter_response_research_question3
* question
 - utter_response_research_question_simple
* technicaldesign
 - utter_response_architecture

## corona
* corona 
 - action_fetch_corona

## weather
* ask_weather
 - action_response_weather

## InsuranceCHeck

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* inform{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - action_fetch_corona
    - slot{"coronaCases":480682}
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":2}
    - insurance_check
    - slot{"travel_days":2}
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* inform{"age":"1988"}
    - slot{"age":"1988"}
    - insurance_check
    - slot{"age":32}
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}

## BeerDrinking
* beer
 - utter_response_beer

## RKI
* rki_risk
 - action_RKIWarning

## CoronaDetails
* rki_risk 
- action_RKIWarning
* ask_rki 
- utter_answer_rki
* ask_quarantaine
- utter_answer_quarantane
* ask_corona_test_location
- utter_answer_coronaLocation

## Story from conversation with f72ca144a712464bad307f4bcacff42b on November 23rd 2020

* greet
    - utter_greet
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* inform{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* ask_rki
    - utter_answer_rki
* ask_quarantaine
    - utter_answer_quarantane
* ask_corona_test_location
    - utter_answer_coronaLocation
    - slot{"destination":"Indien"}
    - utter_ask_continue
* affirm
    - insurance_check
    - slot{"requested_slot":"travel_days"}

## MeaningOfLife
* meaningoflife
- utter_answer_meaningoflife

## travel_tipps
* travel_tipps
- utter_answer_destinationTipps

## Restart Bot 
* restart
- action_restart_bot

## ExplaiNDestination
* ask_whydestination
- utter_explain_whyDestination

## New Story

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* ask_whydestination
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"destination"}

## ExplainTravelDays
* ask_whyTravelDays
- utter_explain_whyTravelDays

## ExplainLuggage
* ask_whyLuggage
- utter_explain_whyBaggeLoss

## ExplainFinanceLoss
* ask_whyFinanceLoss
- utter_explain_whyFinanceLoss

## ExplainGroup
* ask_whyGroup
- utter_explain_whyGroup

## New Story

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* inform{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* ask_whyTravelDays
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":12}
    - insurance_check
    - slot{"travel_days":12}
    - slot{"requested_slot":"luggage"}
* ask_whyLuggage
    - utter_explain_whyBaggeLoss
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* ask_whyFinanceLoss
    - utter_explain_whyFinanceLoss
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
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
* ask_whyGroup
    - utter_explain_whyGroup
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"age":"1988"}
    - insurance_check
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Asien"}

## ExplainAge
* ask_whyAge
- utter_explain_whyAge

## ExplainMoreTravel
* ask_whyMoreTravel
- utter_explain_whyMoreTravel

## New Story

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* ask_whydestination
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"destination"}
* inform{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* ask_whyTravelDays
    - utter_explain_whyTravelDays
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":20}
    - insurance_check
    - slot{"travel_days":20}
    - slot{"requested_slot":"luggage"}
* ask_whyLuggage
    - utter_explain_whyBaggeLoss
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* ask_whyFinanceLoss
    - utter_explain_whyFinanceLoss
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* ask_whyMoreTravel
    - utter_explain_whyMoreTravel
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* ask_whyAge
    - utter_explain_whyAge
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"requested_slot":"age"}
* inform{"age":"1988"}
    - slot{"age":"1988"}
    - slot{"age":"1988"}
    - insurance_check
    - slot{"age":32}
    - slot{"requested_slot":"group"}
* ask_whyGroup
    - utter_explain_whyGroup
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"age":"1988"}
    - insurance_check
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Asien"}

## PPI
* ppi
- utter_answer_ppi
