import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button").click()
time.sleep(4)
# driver.switch_to_alert().accept()  # clicks on OK button on alert box
driver.switch_to_alert().dismiss() # Clicks on Cancel Button on Alert box
time.sleep(5)
driver.close()
