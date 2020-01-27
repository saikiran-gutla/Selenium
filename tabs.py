"""This program is used to switch between the tags among the browsers"""
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

print("Current window handle ID :", driver.current_window_handle)

handles = driver.window_handles  # returns all the values of the opened tabs in the browser
print("Total handles : ", len(handles))
for handle in handles:
    print("Handle :", handle)
    driver.switch_to.window(handle)
    print("Handle Title : ", driver.title)
    if driver.title == "Frames & windows":
        driver.close()
driver.quit()
