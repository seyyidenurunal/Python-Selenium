from sre_constants import ASSERT_NOT
from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


s = Service("C://chromedriver.exe")
driver = webdriver.Chrome(service=s)
url ="https://www.trendyol.com/"

driver.get(url)
print(driver.title)

driver.maximize_window()
time.sleep(1)

close = driver.find_element(By.CLASS_NAME, "modal-close")
close.click()
search = driver.find_element(By.CLASS_NAME, "search-box")
search.send_keys("Gece Lambası")
search.send_keys(Keys.ENTER)

page = driver.find_element(By.CLASS_NAME, "prdct-cntnr-wrppr")
page.click()

product = driver.find_element(By.CLASS_NAME, "image-overlay")
product.click()

driver.switch_to.window(driver.window_handles[1])

addToCard = driver.find_element(By.XPATH, "//*[@id='product-detail-app']/div/div[2]/div[1]/div[2]/div[2]/div[5]/button")
addToCard.click()

time.sleep(1)

accountBasket = driver.find_element(By.XPATH, "//*[@id='account-navigation-container']/div/div[2]/a")
accountBasket.click()

