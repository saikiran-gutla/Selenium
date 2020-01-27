import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")

driver.get("https://data.worldbank.org/country")
print(driver.title)
driver.maximize_window()

# 1) Scroll Upto particular pixels
# driver.execute_script("window.scrollBy(0,1000)", "")

# 2) Scroll Until the Element found in the page
element = driver.find_element_by_xpath("//*[@id='main']/div[2]/section[9]/ul/li[2]/a")
driver.execute_script("arguments[0].scrollIntoView();", element)

# 3) Scroll till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

time.sleep(10)
