import json
import statistics

import jsonpath
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://weather.com/")
time.sleep(10)
driver.find_element_by_id("LocationSearch_input").send_keys("Del")
driver.implicitly_wait(6)
cities = driver.find_elements_by_xpath("//div[@id='LocationSearch_listbox']//button")

print(len(cities))

for city in cities:
    if city.text == "Delhi":
        print(city.text)
        city.click()
        driver.implicitly_wait(6)
        break

time.sleep(8)
xyz = driver.find_element_by_css_selector("h1[class='CurrentConditions--location--kyTeL']")
uvw = xyz.text
driver.implicitly_wait(8)
temp = driver.find_element_by_xpath("//div[@class='CurrentConditions--primary--2SVPh']//span")
Temp = str(temp.text)
temperature = Temp.split("°")
print(temperature)
print(temperature[0])
Temptest = 273 + int(temperature[0])
print(uvw)
print(Temptest)
assert "Delhi" in uvw

url = "https://api.openweathermap.org/data/2.5/weather?q=Delhi&appid=1945225a7ae204cada41af0e11968757"

# send request

response = requests.get(url)
# display content
json_data = json.loads(response.text)
print(json_data)
temp = jsonpath.jsonpath(json_data, 'main.temp')
# temp_data = json_data("main.temp")
print(temp)
# assert response.status_code == 200

# assert temp == Temptest
temp.append(Temptest)
print(temp)
var_temp = statistics.variance(temp)
print(var_temp)
Range = 5
if var_temp <= Range:
    print("Variances in Range")
else:
    print(" Temperature Difference is High ")
