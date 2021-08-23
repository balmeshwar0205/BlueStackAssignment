# API URL
import json

import jsonpath
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=1945225a7ae204cada41af0e11968757"

# send request

response = requests.get(url)
# display content
json_data = json.loads(response.text)
print(json_data)
temp=jsonpath.jsonpath(json_data,'main.temp')
#temp_data = json_data("name")
print(temp)

assert response.status_code == 200



