from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as wait

#test file to scroll and select all the links under a state

PATH = "C:\Program Files\Drivers\chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)
driver.get('https://www.redbus.in/online-booking/ksrtc-kerala/?utm_source=rtchometile')
driver.maximize_window()




time.sleep(2)
all_routes =  driver.find_elements(By.XPATH,"//div[@class='route_link']")

for route in all_routes:
        try:
            route_name = route.find_element(By.XPATH,".//a[@class='route']")
            driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", route_name)
            driver.execute_script("arguments[0].style.border='3px solid red'", route_name) 
            time.sleep(5)
        except NoSuchElementException:
            print("error")






