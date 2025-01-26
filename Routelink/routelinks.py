from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait


PATH = "C:\Program Files\Drivers\chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)

route_details = []
Link = []

driver.get('https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile')

time.sleep(5)

all_routes =  driver.find_elements(By.XPATH,"//div[@class='route_link']")

for route in all_routes:
        try:
            route_name = route.find_element(By.XPATH,".//a[@class='route']")
            # route_link = route_name.get_attribute("href")
            route_details.append(route_name.text)
            
        except NoSuchElementException:
            route_details.append("NA")

            
        try:
            route_link = route_name.get_attribute("href")
            Link.append(route_link)
        except NoSuchElementException:
            Link.append("NA")


df = pd.DataFrame(zip(route_details,Link),columns=["Route","Link"])
df.to_excel('Routes.xlsx')

# driver.find_element(By.XPATH,"//a[@class='route']").click()
# 
# height = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


