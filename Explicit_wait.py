import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.expedia.com/")
driver.implicitly_wait(3)
driver.find_element_by_id("tab-flight-tab-hp").click()
# OR CAN USE THE BELOW METHOD TO GET ID
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("BOS")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("JFK")

driver.find_element(By.ID, "flight-departing-hp-flight").clear()
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("02/02/2020")

driver.find_element(By.ID, "flight-returning-hp-flight").clear()
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("05/02/2020")

# driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/button").click()
# NEED TO ADD MORE PASSENGERS
# driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button/span[1]/svg/path[2]").click()
# driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button/span[1]/svg/path[1]").click()
# driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button/span[1]/svg").click()
# driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[2]/div[1]/div[4]/button/span[1]/svg").click()
driver.find_element_by_xpath("//*[@id='gcw-flights-form-hp-flight']/div[7]/label/button").click()

# EXPLICIT WAIT STATEMENTS
wait = WebDriverWait(driver, 15)  # 15 is max time
non_stop_check_box = wait.until(expected_conditions.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
print(non_stop_check_box)
non_stop_check_box.click()
time.sleep(5)
driver.quit()
