import json

filename='_city.json'
data=json.load(open(filename,'r',encoding='utf-8'))

for i in range(len(data)):
    if data[i]['city_name']==u'南京':
        print(data[i]['city_name'],data[i]['city_code'])