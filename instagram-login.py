from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get("https://www.instagram.com")
time.sleep(5)

username= browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

username.send_keys("********")
password.send_keys("*********")

login = browser.find_element_by_xpath("//*[@id='loginForm']/div/div[3]/button/div")
login.click()

time.sleep(10)

browser.close()
