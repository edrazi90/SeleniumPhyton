from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.chrome.options import Options
import time




#Initialize driver
chrome_options = Options()
service = Service(executable_path="chromedriver.exe",Options=chrome_options)
driver = webdriver.Chrome(service=service)
chrome_options.add_experimental_option("detach", True)




    #Initialize data parameter
userName = "user@yahoo.com.my"
password = "password121"
home = "Johor Baharu"
travelDestination = "Singapore"
departDate = "29122024"#DDMMYY 
returnDate = "03122024"#DDMMYY 
passengerTotal = "2"



#Navigate to URL
driver.get("https://www.airasia.com/en/gb")
driver.maximize_window()

#Initialize input parameter needed for homepage
login = driver.find_element(By.ID,"login-component")
tripType = driver.find_element(By.ID,"home_triptype")
paxSection = driver.find_element(By.ID,"airasia-dropdown-options-title")
origin = driver.find_element(By.ID,"origin")
destination = driver.find_element(By.ID,"home_flyingfrom")
depart_date = driver.find_element(By.ID,"departclick-handle")
return_date = driver.find_element(By.ID,"returnclick-handle")
search_button = driver.find_element(By.ID,"home_Search")


#wait til HomePage is displayed
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located((By.ID,"login-component"))
)


"""
#Select trip type
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(tripType))
tripType.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,"TripTypes__Label-sc-1xgnhxw-2 hYKgAZ")))
oneWay = driver.find_element(By.CLASS_NAME,"TripTypes__Label-sc-1xgnhxw-2 hYKgAZ")#declare trip type with ID here
oneWay.click()
WebDriverWait(driver,10)
"""
"""
#Set pax and travel class
paxSection.click()
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,"home_premium_economy")))
premiumEcon = driver.find_element(By.ID,"home_premium_economy")#Initialize Travelclass
premiumEcon.click()
"""

"""
#clear origin & desination  textbox
origin.sendKeys(Keys.CONTROL + "a")
origin.sendKeys(Keys.DELETE)

destination.sendKeys(Keys.CONTROL + "a")
destination.sendKeys(Keys.DELETE)
"""

#Input origin 

WebDriverWait(driver, 5).until(EC.element_to_be_clickable(origin))  # Ensure the element is clickable
origin.click()
time.sleep(5)

promoBanner = driver.find_element(By.ID,"wzrk-cancel")#Click cancel when promo banner appeared
promoBanner.click()
time.sleep(5)

origin.click()
time.sleep(5)
clearOrigin = driver.find_element(By.ID,"flight-place-picker").clear()
time.sleep(5)
origin.send_keys(home)
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
origin.send_keys(Keys.ENTER)


#Input destination
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(destination))
destination.click()
time.sleep(5)
"""
promoBanner = driver.find_element(By.ID,"wzrk-cancel")#Click cancel when promo banner appeared
promoBanner.click()
"""
time.sleep(5)
destination.clear()
destination.send_keys(travelDestination)
"""
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'suggestions')]")))  # Wait for suggestions to appear
"""
destination.send_keys(Keys.ENTER)
time.sleep(5)

#Input depart and destination date 
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(depart_date))
depart_date.send_keys(departDate)
time.sleep(5)
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(return_date))
return_date.send_keys(returnDate)
time.sleep(5)


#Input passenger
passenger_input = driver.find_element(By.ID, "flight-pax-adult")
passenger_input.clear()
passenger_input.send_keys(passengerTotal) 
passenger_input.send_keys(Keys.ENTER)

#Click search button
search_button.click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "flight-results")))

