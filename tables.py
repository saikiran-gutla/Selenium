from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("file:///C:/Users/saikiran/Desktop/Vijay Project/Selenium/sample_tables_example.html")

rows = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr"))
columns = len(driver.find_elements_by_xpath("/html/body/table/tbody/tr[1]/th"))
print(rows, columns)

print("Name \t \t Salary")
print(20 * "=")
for row in range(2, rows + 1):
    for col in range(1, columns + 1):
        value = driver.find_element_by_xpath("/html/body/table/tbody/tr[" + str(row) + "]/td[" + str(col) + "]").text
        print(value, end="       ")
    print()
driver.close()
