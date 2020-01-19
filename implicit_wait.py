from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Selenium Drivers\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.implicitly_wait(10)
user_name = "mercury"
password = "mercury"
uname = driver.find_element_by_name("userName")
pwd = driver.find_element_by_name("password")

uname.send_keys(user_name)
pwd.send_keys(password)
driver.find_element_by_name("login").click()
driver.close()