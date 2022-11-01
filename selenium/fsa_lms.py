from selenium import webdriver
from selenium.webdriver.common.by import By
import fsasetup as fsa

driver = webdriver.Chrome()
driver.get("https://learn.fullstackacademy.com")
driver.implicitly_wait(0.5)
signup_tab = driver.locate_with(By.TAG_NAME, "div").above({By.CLASS_NAME, "m0"})
signup_tab.clickAt()
fname_box = driver.find_element(By.NAME, "firstName")
fname_box.send_keys(fsa.process_form("Name").split(" ")[0])
lname_box = driver.find_element(By.NAME, "lastName")
lname_box.send_keys(fsa.process_form("Name").split(" ")[1])