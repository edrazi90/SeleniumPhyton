from Main import driver,depart_date,return_date,userName,password,webdriver,WebDriverWait,EC,By,time,login
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementNotInteractableException, StaleElementReferenceException, WebDriverException



#verify flight list page is displayed
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"journey-header-container")))

#Verify and select the first flight schedule
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"Container__ContainerWrapper*")))
selectButton = driver.find_element(By.XPATH,"Button__ButtonContainer-sc-7xd2ll-0 ezxQeV")
time.sleep(5)
selectButton.click()
time.sleep(10)


#Press login section and login to the system
login.click()
time.sleep(5)

#Login banner paremeter
mailTextbox = driver.find_element(By.ID,"text-input--login")
passwordTextbox =driver.find_element(By.ID,"password-input--login")
loginButton = driver.find_element(By.ID,"loginbutton")

WebDriverWait(driver, 10).until(EC.element_to_be_clickable(mailTextbox))
mailTextbox.send_keys(userName)
time.sleep(5)
passwordTextbox.send_keys(password)
time.sleep(5)
loginButton.click()
time.sleep(5)







