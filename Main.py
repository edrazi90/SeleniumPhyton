from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.chrome.options import Options
import time
#from Flights_utils import driver,departDate,returnDate,home,travelDestination,passengerTotal,selectRecord
#from Flights_utils import basicDomestic,BasicInternational,internationalTravel,basicIntlSG,verifyLink,selectCard

chrome_options = Options()
service = Service(executable_path="chromedriver.exe",Options=chrome_options)
driver = webdriver.Chrome(service=service)

#wait til HomePage is displayed
WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME,"multiselect AirportPicker-from multiselect-main AirportPicker-from")))


#Initialize data parameter
SiteURL = "https://www.malaysiaairlines.com/my/en/home.html"
userName = "user@yahoo.com.my"
password = "password121"
home = "Alor Setar"
travelDestination = "Kuala Lumpur"
departDate = "2024-01-12"#YYYYDDMM 
returnDate = "2024-03-12"#YYYYDDMM 
passengerTotal = "2"

#Basic insurance handbook
"""MY"""
basicDomestic = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_Domestic.pdf")
BasicInternational= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_International.pdf")
internationalTravel= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_GOM_Travel Protection_MY_International_PW.pdf")

"""SG"""
basicIntlSG = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../msig/mag/sg/doc/insurance/Policy_Wording_bundle.pdf")



#Navigate to URL
driver.get("https://www.malaysiaairlines.com/my/en/home.html")
driver.maximize_window()

#wait til HomePage is displayed
WebDriverWait(driver, 15)

#Accept cookie 
try:
    cookie_accept_button = driver.find_element(By.XPATH, "//button[text()='Accept All']")
    cookie_accept_button.click()
except:
    print("No cookie pop-up found")

#Initialize input parameter needed for Homepage
origin = driver.find_element(By.CLASS_NAME,"multiselect AirportPicker-from multiselect-main AirportPicker-from")
destination = driver.find_element(By.CLASS_NAME,"picker-wrapper picker-wrapper-to")
depart_date = driver.find_element(By.CLASS_NAME,"picker-wrapper picker-wrapper-from")
return_date = depart_date = driver.find_element(By.CLASS_NAME,"picker-wrapper picker-wrapper-to")
search_button = driver.find_element(By.CLASS_NAME,"mt-0")


"""
#clear origin & desination  textbox
origin.sendKeys(Keys.CONTROL + "a")
origin.sendKeys(Keys.DELETE)

destination.sendKeys(Keys.CONTROL + "a")
destination.sendKeys(Keys.DELETE)
"""


"""Main Page"""

#Input origin 
WebDriverWait(driver, 5).until(EC.element_to_be_clickable(origin))  # Ensure the element is clickable
origin.click()
time.sleep(5)
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
passenger_input = driver.find_element(By.CLASS_NAME,"PassengerAndCabinClass")
passenger_input.click()
time.sleep(5)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "input mx-2")))
passenger_input.send_keys(passengerTotal) 
passenger_input.send_keys(Keys.ENTER)

#Click search button
time.sleep(5)
search_button.click()



"""Booking flight page"""

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "ng-star-inserted")))
#Verify if the first record are visible
departure_time = driver.find_elements(By.CLASS_NAME,"upsell-premium-row-pres-container panel-show")

"""Select record with Economy Class if first record are visible"""
records = driver.find_element(By.TAG_NAME,"refx-upsell-premium-row-pres")
economyClass = driver.find_elements(By.CLASS_NAME,"mat-mdc-button-ripple")

for selectRecord in records:
    if economyClass in records.is_displayed():
        selectRecord = driver.find_element(By.XPATH,"//mat-accordion[@class='ng-star-inserted']/refx-upsell-premium-row-pres[0]")
        selectRecord.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "mat-expansion-panel expanded-section ng-tns-c857250080-10 mat-expanded ng-star-inserted")))

"""Verify if expansion panel  and enomony Flex card is displayed"""
expPanel= driver.find_element(By.TAG_NAME,"mh-carousel")
economyFlex = driver.find_element(By.CLASS_NAME,"refx-price-card fare-family-ECOFLXXYMY cabin-eco ng-star-inserted")

for selectCard in expPanel:
    if economyFlex in expPanel.is_displayed():
        economyFlex.screenshot('/Screenshots/EconomyFlex.png')


"""Verify if Basic Travel Insurance is listed in the selected card list"""
list = driver.find_element(By.TAG_NAME,"li")
basicTravel = driver.find_elements(By.ID,"REFX-FARE-FAMILY.ALL.POLICY-BENEFIT") 

for verifyLink in list:
    if basicTravel in list.is_displayed():
        basicTravelLink = driver.find_element(By.PARTIAL_LINK_TEXT,'https://static.prod-eu.wl.ancileo.com/anc/mag/all/doc/index.html')
        basicTravelLink.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "understand-cover-main")))


"""Verify all basic Travel TnC document are displayed"""
basicDomestic.is_displayed()
BasicInternational.is_displayed()
internationalTravel.is_displayed()
basicIntlSG.is_displayed()




