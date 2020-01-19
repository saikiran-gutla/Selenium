from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")

# RADIO BUTTONS
radio_button = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input")
print(radio_button.is_selected())
radio_button = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input").click()
radio_button = driver.find_element(By.XPATH, "//*[@id='basicBootstrapForm']/div[5]/div/label[1]/input")
print(radio_button.is_selected())

# CHECK BOXES
check_box = driver.find_element(By.ID, "checkbox2").is_selected()
print(check_box)
check_box = driver.find_element(By.ID, "checkbox2").click()
check_box = driver.find_element(By.ID, "checkbox2").is_selected()
print(check_box)

# DROP DOWN MENUS
# We can Use Select class for this , can be imported from the selenium
drop_down = driver.find_element_by_id("Skills")
options = Select(drop_down)
# CAN BE DONE IN 3 WAYS
# 1) Select by visible text
# options.select_by_visible_text('C')
# 2) SELECT BY INDEX
# options.select_by_index(2)
# 3) Select by Value
options.select_by_value('C++')  # value of the element tag

all_options = options.options  # options is an inbuilt object
print(len(all_options))
print(all_options)  # returns all objects in list format
for i in all_options:
    print(i.text)  # need to print the value by using text

# href tags
links = driver.find_elements(By.TAG_NAME, 'a')
print(f'TOTAL LINKS IN TH PAGE: {len(links)}')
for link in links:
    print(link.text)
# driver.find_element(By.LINK_TEXT, "WebTable").click()  # the text of the anchor value
driver.find_element(By.PARTIAL_LINK_TEXT, "Web").click()  # can give some text from the word
time.sleep(10)
driver.close()
