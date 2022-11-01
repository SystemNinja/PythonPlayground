# First script in selenium
# Ref: https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.title # => "Google"
driver.implicitly_wait(0.5)
search_box = driver.find_element(By.NAME, "q")
search_button = driver.find_element(By.NAME, "btnK")
search_box.send_keys("Selenium")
search_button.click()
driver.find_element(By.NAME,"q").get_attribute("value")
driver.quit()