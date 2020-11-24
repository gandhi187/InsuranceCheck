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

## New Story2

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* question
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"destination"}
* inform{"destination":"Indien"}
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
* travel_days{"duration":2}
    - insurance_check
    - slot{"travel_days":14}
    - slot{"requested_slot":"luggage"}
* question
    - slot{"destination":"Indien"}
    - utter_explain_whyBaggeLoss
    - insurance_check
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* question
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - utter_explain_whyFinanceLoss
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* question
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - utter_explain_whyMoreTravel
    - insurance_check
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* question
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - utter_explain_whyAge
    - insurance_check
    - slot{"requested_slot":"age"}
* inform{"age":"1989"}
    - slot{"age":"1989"}
    - slot{"age":"1989"}
    - insurance_check
    - slot{"age":31}
    - slot{"requested_slot":"group"}
  	- insurance_check
  	- form{"name": "insurance_check"}

## interactive_story_1
* affirm
    - insurance_check
    - form{"name": "insurance_check"}
    - slot{"requested_slot": "destination"}
* question
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot": "destination"}
* form: inform{"destination": "Türkei"}
    - slot{"destination": "Türkei"}
    - form: insurance_check
    - slot{"destination": "Türkei"}
    - slot{"requested_slot": "travel_days"}
* question
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot": "travel_days"}
* form: travel_days{"duration": 3}
    - form: insurance_check
    - slot{"travel_days": 3}
    - slot{"requested_slot": "luggage"}
* question
    - utter_explain_whyBaggeLoss
    - insurance_check
    - slot{"requested_slot": "luggage"}

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

## Story from conversation with cfb4364acde549928496f18285135128 on November 18th 2020

* greet
    - utter_greet
* affirm
    - insurance_check
    - action_fetch_continent
* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* question
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"destination"}
* inform{"destination":"USA"}
    - slot{"destination":"USA"}
    - slot{"destination":"USA"}
    - insurance_check
    - slot{"destination":"USA"}
    - slot{"requested_slot":"travel_days"}
* question
    - slot{"destination":"USA"}
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":2}
    - insurance_check
    - slot{"travel_days":14}
    - slot{"requested_slot":"luggage"}
* question
    - slot{"destination":"USA"}
    - utter_explain_whyBaggeLoss
    - insurance_check
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* question
    - slot{"destination":"USA"}
    - slot{"luggage":"mittel"}
    - utter_explain_whyFinanceLoss
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* question
    - slot{"destination":"USA"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - utter_explain_whyMoreTravel
    - insurance_check
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* inform{"age":"1977"}
    - slot{"age":"1977"}
    - slot{"age":"1977"}
    - insurance_check
    - slot{"age":43}
    - slot{"requested_slot":"group"}
* question
    - slot{"destination":"USA"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"age":"1977"}
    - utter_explain_whyGroup
    - insurance_check
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}
    - action_fetch_continent
    - slot{"continent":"Nordamerika"}

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

## Story from conversation with b81740a633bb468ebd8ffec32a96bbb2 on November 23rd 2020

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* inform{"destination":"italien"}
    - slot{"destination":"italien"}
    - slot{"destination":"italien"}
    - insurance_check
    - slot{"destination":"italien"}
    - slot{"requested_slot":"travel_days"}
* ask_rki
    - utter_answer_rki
* ask_quarantaine
    - utter_answer_quarantane
* ask_corona_test_location
    - utter_answer_coronaLocation
    - utter_ask_continue
* affirm
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* question
    - slot{"destination":"italien"}
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":2}
    - insurance_check
    - slot{"travel_days":60}
    - slot{"requested_slot":"moreTravel"}
* question
    - slot{"destination":"italien"}
    - utter_explain_whyMoreTravel
    - insurance_check
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
* question
    - slot{"destination":"italien"}
    - slot{"age":"1988"}
    - utter_explain_whyGroup
    - insurance_check
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}

## New Story1

* affirm
    - insurance_check
    - form{"name":"insurance_check"}
    - slot{"requested_slot":"destination"}
* question
    - utter_explain_whyDestination
    - insurance_check
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
    - utter_ask_continue
* affirm
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* question
    - slot{"destination":"Indien"}
    - utter_explain_whyTravelDays
    - insurance_check
    - slot{"requested_slot":"travel_days"}
* inform{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - insurance_check
    - slot{"destination":"Indien"}
    - slot{"requested_slot":"travel_days"}
* travel_days{"duration":20}
    - insurance_check
    - slot{"travel_days":20}
    - slot{"requested_slot":"luggage"}
* inform{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - slot{"luggage":"mittel"}
    - insurance_check
    - slot{"luggage":"mittel"}
    - slot{"requested_slot":"financeLoss"}
* question
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - utter_explain_whyFinanceLoss
    - insurance_check
    - slot{"requested_slot":"financeLoss"}
* inform{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - slot{"financeLoss":"mittel"}
    - insurance_check
    - slot{"financeLoss":"mittel"}
    - slot{"requested_slot":"moreTravel"}
* question
    - slot{"destination":"Indien"}
    - slot{"destination":"Indien"}
    - slot{"luggage":"mittel"}
    - slot{"financeLoss":"mittel"}
    - utter_explain_whyMoreTravel
    - insurance_check
    - slot{"requested_slot":"moreTravel"}
* deny
    - insurance_check
    - slot{"moreTravel":false}
    - slot{"requested_slot":"age"}
* question
    - utter_explain_whyDestination
    - insurance_check
    - slot{"requested_slot":"age"}
* inform{"age":"1987"}
    - slot{"age":"1987"}
    - insurance_check
    - slot{"age":33}
    - slot{"requested_slot":"group"}
* deny
    - insurance_check
    - slot{"group":false}
    - form{"name":null}
    - slot{"requested_slot":null}

## MeaningOfLive
* meaningoflive
- utter_answer_meaningoflife

## travel_tipps
* travel_tipps
- utter_answer_destinationTipps

## Restart Bot 
* restart
- action_restart_bot
