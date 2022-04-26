import requests
import pandas
import json
import csv

url = 'https://oxenfurt.constructionmonitor.com:9200/construction_type_training_data/_search'
myobj = {'somekey': 'somevalue'}

i = 0
allTypes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26', '27', '28',
            '29', '31', '32', '33', '34', '35', '36', '38', '40',
            'DISH', 'EVENT', 'INSPECTION', 'OCCUPANCY', 'POLE',
            'SCREENWALL', 'SHADE', 'SIDING', 'SIGN', 'TEMP',
            'WASHERDRYER', 'CODE', 'AFTERTHEFACT']
for x in allTypes:
    x = requests.post(url, auth = ('tayloryoung', 'cc1119969'), json = {
        "size" : 5000,
        "sort" : [
            {"reviewed" : "desc"},
            "priority"
        ],
        "aggs" : {
            "types_count" : {"value_count" : {"field" : "_id"}}
        },
        "query":{  
            "bool":{ 
                "must":[
                    {"match" :{
                        "constructionTypeID":allTypes[i]
                    }},    
                    {"match" :{
                        "reviewed":True
                    }}
                ]
            }
        }
    })
    fileName = allTypes[i] + "training_data.json"
    with open(fileName, 'w') as outfile:
        json.dump(x.json(), outfile)
    i+=1
