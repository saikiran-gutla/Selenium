"""THIS SCRIPT TAKES THE NAME TO BE SEARCHED ON YOUTUBE AND PLAYS THE FIRST VIDEO LISTED IN THE RESULTS ORDER"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import keyboard

driver = webdriver.Firefox(executable_path="C:\Selenium Drivers\geckodriver-v0.26.0-win64\geckodriver.exe")
driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys("Aladeen Mother Fucker")
driver.find_element_by_id("search-icon-legacy").click()
videos = driver.find_elements_by_id("video-title")
print(len(videos))
driver.find_element_by_link_text(videos[0].text).click()
for video in videos:
    print(video.text)
driver.maximize_window()

keyboard.press_and_release('f')

wait = WebDriverWait(driver, 350)  # 15 is max time
non_stop_check_box = wait.until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "ytp-play-button ytp-button")))

driver.quit()
