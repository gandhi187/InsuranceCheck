import psycopg2
import json
from datetime import date

def queryDB(travel_days,luggage,financeLoss,moreTravel,age,group,occasionDetails,destination):
        if luggage=="niedrig" or luggage == None:
                luggage=''
        if luggage =="hoch":
                luggage = 'mittel'
        if financeLoss == "niedrig" or financeLoss == None:
                financeLoss=''
                print('none')
        if financeLoss == 'hoch':
                financeLoss = 'mittel'
        print ("Finance Loss : " + financeLoss)
        print ("Baggage : " + luggage)
        try:
            x =  {   "type": "template",     "payload": {            "template_type": "generic",            "elements": [            ]        }    }
            temp = x['payload']['elements']

            connection = psycopg2.connect(user="admin",
                                    password="IUnwrDPfBiZB4c0",
                                    host="54.84.180.45",
                                    port="32768",
                                    database="insurance")
            cursor = connection.cursor()
            postgreSQL_select_Query = "select name, image_link from insuranceproducts WHERE age >=" + str(age) + "AND luggage ="+"'" +luggage +"'" + " AND finance_loss =" + "'"+ financeLoss + "'" + " AND person_group = " + str(group) + " AND " + str(travel_days) + "  <= travel_days UNION select name, image_link from insuranceproducts where name like '%Auslandsreisekranken%' AND person_group = " + str(group) + " and  more_travel = " + str(moreTravel) + " AND " + str(travel_days) + " <= travel_days"
            print("Query : " + postgreSQL_select_Query)
            cursor.execute(postgreSQL_select_Query)
            print("Selecting rows from mobile table using cursor.fetchall")
            mobile_records = cursor.fetchall() 
            print("Print each row and it's columns values")
            for row in mobile_records:
                y = {
                "title": row[0],
                "subtitle":destination,
                "image_url": row[1],
                "buttons": [{
                    "title": "Mehr",
                    "url": row[1],
                    "type": "web_url"
                },
                    {
                        "title": "Interessant",
                        "type": "postback",
                        "payload": "/greet"
                    }
                ]
            }
                temp.append(y)
                print("Id = ", row[0], )
                print("Model = ", row[1],"\n")
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)

        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                print(x)
                return x


queryDB("50",None,None,False,"50",False,"Studentenfahrt","asd")




    # def getInsurance(recommendation){

    #     if (int(travel_days) >= 45 and <= 135):
    #         if (moreTravel == False and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' and group == True):
    #             print ('Kombi Packet Einmalig Gruppe')
    #         if (moreTravel == False and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' and group == False):
    #             print ('Kombi Packet Einmalig Einzelnd')
    #     elif (int (travel_days) >= 45):
    #         if (moreTravel == False and luggage == 'niedrig' and financeLoss == 'mittel' or financeLoss = 'hoch'  and group == False and int(age) <=34):
    #             print ("Studenten Exklusiv")
    #         if (moreTravel == False and luggage == 'niedrig' and financeLoss == 'niedrig' and group == False and int(age) <=34):
    #             print ("Stundenten Langzeit)")
    #         else:
    #             print ("Auslandsversicherung langzeit")
    #     elif (int (travel_days <= 45)):
    #         if (moreTravel == True and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' and group == True):
    #             print ("Kombi Paket Jahres Gruppe ")
    #         if (moreTravel == True and luggage == 'hoch' and financeLoss == 'hoch' or luggage == 'mittel' or financeLoss =='mittel' and group == False):
    #             print ("Kombi Paket Jahres Einzelnd ")
    
    # }