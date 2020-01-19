import time
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")

driver.get("https://www.google.com/chrome/?brand=CHBD&gclid=Cj0KCQiA9orxBRD0ARIsAK9JDxRiXgr1Eyr2Ecn3JQhtMq809_etcWMXInu2SfvBx_mAo_myOTQoi6QaAm41EALw_wcB&gclsrc=aw.ds")
print(driver.title)
driver.get("https://www.opera.com/?utm_campaign=%2307%20-%20IN%20-%20Search%20-%20EN%20-%20Branded%20-%202017&gclid=Cj0KCQiA9orxBRD0ARIsAK9JDxRnNXbPZJCHPRA0mehj8c0WLDgKUSEuttrhf8IRHAiKNDR6vNaKUo4aAmzzEALw_wcB")

print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
time.sleep(10)
driver.refresh()
time.sleep(5)
driver.save_screenshot("hello.png")

driver.close()
