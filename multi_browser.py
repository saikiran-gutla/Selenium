from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path="C:\Selenium Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
# driver = webdriver.Opera(executable_path="C:\Selenium Drivers\operadriver_win64\operadriver.exe")
driver.get("http://newtours.demoaut.com/")
print(driver.title)  # prints titile of the page
print(driver.current_url)
print(driver.page_source)
driver.close()
