from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://demo.automationtesting.in/")
print(driver.title)
driver.find_element_by_xpath("//*[@id='enterimg']").click()
driver.close()
# driver.quit()  # currently focused browser will be closed
