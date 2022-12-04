import json
import requests
from pprint import pprint

# get JSON string data from CityBike NYC using web requests library
json_response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
# check type of json_response object
print(json_response)
print(type(json_response.text))
md = json.loads(json_response.text)
pprint(md)
#print(json_response.text)
# load data in loads() function of json library
# bike_dict = json.loads(json_response.text)
#check type of news_dict
# print(type(bike_dict))
# now get stationBeanList key data from dict
# print(bike_dict['stationBeanList'])
# bikelist = []
# for i in bike_dict['stationBeanList']:
#     bikelist.append(i)
#
print(md['sprites'])
#
# fulton = bike_dict['stationBeanList'][100]
# print(type(fulton))
# print(fulton['stationName'])


