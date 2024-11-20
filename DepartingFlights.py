from ..SeleniumPhyton import Main





#verify flight list page is displayed
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"journey-header-container")))


