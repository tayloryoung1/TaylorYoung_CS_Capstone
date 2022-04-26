import json
import csv
import pandas as pd

allTypes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
            '11', '12', '13', '14', '15', '16', '17', '18', '19',
            '20', '21', '22', '23', '24', '25', '26', '27', '28',
            '29', '31', '32', '33', '34', '35', '36', '38', '40',
            'DISH', 'EVENT', 'INSPECTION', 'OCCUPANCY', 'POLE',
            'SCREENWALL', 'SHADE', 'SIDING', 'SIGN', 'TEMP',
            'WASHERDRYER', 'CODE', 'AFTERTHEFACT']

csvFile = open('csvTrain.csv', 'w', newline = '')
writer = csv.writer(csvFile)
header = ['category', 'text']
writer.writerow(header)

i = 0
for x in allTypes:
    fileName = allTypes[i] + "training_data.json"
    with open(fileName, encoding = "ISO-8859-1") as json_file:
        data = json.load(json_file)

    info = data['hits']['hits']
    for x in info:
        des = x['_source']['string']
        row = [x['_source']['constructionTypeID'], des]
        writer.writerow(row)

    i+=1

csvFile.close

df = pd.read_csv('csvTrain.csv', encoding = "ISO-8859-1") # avoid header=None. 
shuffled_df = df.sample(frac=1)
shuffled_df.to_csv('csvTrain.csv', index=False)
