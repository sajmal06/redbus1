from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait as w



PATH = "C:\Program Files\Drivers\chromedriver.exe"

service = Service(executable_path=PATH)

driver = webdriver.Chrome(service=service)
wait = w(driver,timeout=10)
actions = ActionChains(driver)
Name = []
Type = []
Start = []
Duration = []
End = []
Rating = []
Cost = []
Seats_avail = []


driver.get('https://www.redbus.in/bus-tickets/thiruvananthapuram-to-kozhikode?fromCityId=71425&toCityId=74661&fromCityName=Trivandrum&toCityName=Calicut&busType=Any&srcCountry=IND&destCountry=IND&onward=21-Jan-2025')
driver.maximize_window()

# w(driver, 10).until(
#     EC.visibility_of_element_located((By.CLASS_NAME, "bus-item"))
# )
# actions.send_keys(Keys.END).perform()
time.sleep(20)
viewbus = driver.find_element(By.XPATH,"//div[@class='button']")
viewbus.click()
scroll_pause_time = 2
for _ in range(10):  # Number of scrolls
        driver.execute_script("window.scrollBy(0, 1000);")  # Scroll down by 1000 pixels
        time.sleep(scroll_pause_time)


# time.sleep(10)




  # Adjust the range for the number of scrolls needed
           # Press the "Page Down" key



# driver.find_element(By.XPATH,"//a[@class='route']").click()

all_items = driver.find_elements(By.XPATH,"//li[@class='row-sec clearfix']")



for item in all_items:
    
        # time.sleep(0.5)
        try:
            busname = item.find_element(By.XPATH,".//div[@class ='travels lh-24 f-bold d-color']").text
            # driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", busname)
            # time.sleep(1)
            Name.append(busname)
            
           
        except NoSuchElementException:
            Name.append("NA")
        
        try:
            bustype = item.find_element(By.XPATH, ".//div[@class ='bus-type f-12 m-top-16 l-color evBus']").text
            Type.append(bustype)
        except NoSuchElementException:
            Type.append("NA")
        

        try:
            busdeparturetime = item.find_element(By.XPATH,".//div[@class ='dp-time f-19 d-color f-bold']").text
            Start.append(busdeparturetime)
        except NoSuchElementException:
            Start.append("NA")               

        try:
            busduration = item.find_element(By.XPATH,".//div[@class ='dur l-color lh-24']").text
            Duration.append(busduration)
        except NoSuchElementException:
            Duration.append("NA")
        

        try:
            busarraivaltime = item.find_element(By.XPATH,".//div[@class ='bp-time f-19 d-color disp-Inline']").text
            End.append(busarraivaltime)
        except NoSuchElementException:
            End.append("NA")
        

        try:
            busrating = item.find_element(By.XPATH, ".//span[@class='']").text
            Rating.append(busrating)
        except NoSuchElementException:
            Rating.append("NA")
    
        try:
            busprice = item.find_element(By.XPATH, ".//span[@class ='f-19 f-bold']").text
            Cost.append(busprice)
        except NoSuchElementException:
           busprice = item.find_element(By.XPATH, ".//span[@class='f-bold f-19']").text
           Cost.append(busprice)
        
        try:
            busseats = item.find_element(By.XPATH,"//div[@class ='seat-left m-top-30']").text
            Seats_avail.append(busseats)
        except NoSuchElementException:
            Seats_avail.append("0")

       
        
df = pd.DataFrame(zip(Name,Type,Start,Duration,End,Rating,Cost,Seats_avail),columns=["Name","Type","Start","Duration","End","Rating","Cost","Seats_avail"])
df['route'] = 'Thiruvananthapuram to Kozhikode'
df.to_excel('Thiruvananthapuram_to_Kozhikode.xlsx',index=False)

# height = driver.execute_script("return document.body.scrollHeight")
# while True:
#  driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")


print(df)
