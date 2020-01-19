import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://selenium.dev/selenium/docs/api/java/index.html")

driver.switch_to_frame("packageListFrame")  # ATTRIBUTE NAME OF THE FRAME
driver.find_element_by_link_text("com.thoughtworks.selenium.condition").click()

driver.switch_to.default_content()  # GOES BACK TO MAIN PAGE AGAIN

driver.switch_to_frame("packageFrame")
driver.find_element(By.XPATH, "/html/body/div/ul[1]/li[2]/a").click()

driver.switch_to.default_content()
driver.switch_to_frame("classFrame")
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[1]/ul/li[2]/a").click()
driver.close()
