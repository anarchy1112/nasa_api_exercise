
from datetime import timedelta, datetime

import requests
import json

base_url = 'https://api.nasa.gov'
start_date='2023-04-01'
end_date='2023-04-08'
api_key='wXysSgPjigxz1HK8ZfPoe0xFUMbLsPR6Fj2uu8Ca'



neo_endpoint = '/neo/rest/v1/feed?start_date='+start_date+'&end_date='+end_date+'&api_key='+api_key

neo_url=base_url+neo_endpoint

request=requests.get(neo_url)
result=request.json()

# print(json.dumps(result, sort_keys=True, indent=4))

#
# print(json.dumps(result["near_earth_objects"]["2023-02-01"][0]["close_approach_data"][0]["close_approach_date"], sort_keys=True, indent=4))
# print(json.dumps(result["near_earth_objects"]["2023-02-01"][0]["close_approach_data"][0]["orbiting_body"], sort_keys=True, indent=4))
# print(json.dumps(result["near_earth_objects"]["2023-02-01"][0]["is_potentially_hazardous_asteroid"], sort_keys=True, indent=4))
# print(len(result["near_earth_objects"]["2023-02-01"][0]["close_approach_data"]))

start_date = datetime.strptime(start_date, '%Y-%m-%d')

for i in range(1,5):
    curr_date = start_date + timedelta(days=i)
    curr_date_str = curr_date.strftime('%Y-%m-%d')
    for i in range(len(result["near_earth_objects"][curr_date_str])-1):
        if result["near_earth_objects"][curr_date_str][i]["is_potentially_hazardous_asteroid"]==True:
            print('datum prilaska',json.dumps(result["near_earth_objects"][curr_date_str][i]["close_approach_data"][0]["close_approach_date"], sort_keys=True, indent=4), end=' ')
            print('potencijalno opasan', json.dumps(result["near_earth_objects"][curr_date_str][i]["is_potentially_hazardous_asteroid"], sort_keys=True, indent=4), end= ', ')
            print('Ime asteroida', json.dumps(result["near_earth_objects"][curr_date_str][i]['name'], sort_keys=True, indent=4), end=', ')
            print('max veličina u metrima',json.dumps(result["near_earth_objects"][curr_date_str][i]["estimated_diameter"]["meters"]["estimated_diameter_max"], sort_keys=True, indent=4),)