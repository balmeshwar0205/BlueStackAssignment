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
next_page = xyz.text
driver.implicitly_wait(8)
temp = driver.find_element_by_xpath("//div[@class='CurrentConditions--primary--2SVPh']//span")
Temp = str(temp.text)
temperature = Temp.split("°")
# print(temperature)
print(temperature[0])
# temperature conversion to kelvin
Temptest = 273 + int(temperature[0])
print(next_page)
print(Temptest)
assert "Delhi" in next_page
