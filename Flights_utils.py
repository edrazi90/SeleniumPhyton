
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as UC
"""


"""Initialize data parameter
SiteURL = "https://www.malaysiaairlines.com/my/en/home.html"
userName = "user@yahoo.com.my"
password = "password121"
home = "Alor Setar"
travelDestination = "Kuala Lumpur"
departDate = "2024-01-12"#YYYYDDMM 
returnDate = "2024-03-12"#YYYYDDMM 
passengerTotal = "2"
"""

"""MY
basicDomestic = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_Domestic.pdf")
BasicInternational= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_Basic_Travel_Protection_MY_International.pdf")
internationalTravel= driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../etiqa/mag/my/doc/MH_GOM_Travel Protection_MY_International_PW.pdf")
"""
"""SG
basicIntlSG = driver.find_element(By.PARTIAL_LINK_TEXT,"../../../../msig/mag/sg/doc/insurance/Policy_Wording_bundle.pdf")
"""

"""capture all records in the list
records = driver.find_element(By.TAG_NAME,"refx-upsell-premium-row-pres")
economyClass = driver.find_elements(By.CLASS_NAME,"mat-mdc-button-ripple")

for selectRecord in records:
    if economyClass in records.is_displayed():
        selectRecord = driver.find_element(By.XPATH,"//mat-accordion[@class='ng-star-inserted']/refx-upsell-premium-row-pres[0]")
        selectRecord.click()
"""


"""Verify if expansion panel  and enomony Flex card is displayed
expPanel= driver.find_element(By.TAG_NAME,"mh-carousel")
economyFlex = driver.find_element(By.CLASS_NAME,"refx-price-card fare-family-ECOFLXXYMY cabin-eco ng-star-inserted")

for selectCard in expPanel:
    if economyFlex in expPanel.is_displayed():
        economyFlex.screenshot('/Screenshots/EconomyFlex.png')
"""



    
"""Verify if Basic Travel Insurance is listed in the selected card list
list = driver.find_element(By.TAG_NAME,"li")
basicTravel = driver.find_elements(By.ID,"REFX-FARE-FAMILY.ALL.POLICY-BENEFIT") 

for verifyLink in list:
    if basicTravel in list.is_displayed():
        basicTravelLink = driver.find_element(By.PARTIAL_LINK_TEXT,'https://static.prod-eu.wl.ancileo.com/anc/mag/all/doc/index.html')
        basicTravelLink.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "understand-cover-main")))
"""


