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

"""MY"""
basicDomestic = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_Domestic.pdf")
BasicInternational= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_International.pdf")
internationalTravel= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_GOM_Travel Protection_MY_International_PW.pdf")
"""SG"""
basicIntlSG = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../msig/mag/sg/doc/insurance/Policy_Wording_bundle.pdf")


#Capture all records in the list
records = driver.find_element(By.TAG_NAME,"refx-upsell-premium-row-pres")
economyClass = driver.find_elements(By.CLASS_NAME,"mat-mdc-button-ripple")

for selectRecord in records:
    if economyClass in records.is_displayed():
        selectRecord = driver.find_element(By.XPATH,"//mat-accordion[@class='ng-star-inserted']/refx-upsell-premium-row-pres[0]")
        selectRecord.click()