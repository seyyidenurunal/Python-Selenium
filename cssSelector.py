from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()

options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path=r"C:/Users/tiplay/Desktop/chromedriver.exe",options=options)

url = 'https://www.emlakjet.com/ilan/kelepir-21-ara-kat-ici-sifir-sik-dekorlu-yuksek-kira-garantili-hemen-arayin-12046772/'

driver.get(url)

time.sleep(2)

driver.maximize_window()
time.sleep(2)

ilanBilgileri = driver.find_elements(By.CSS_SELECTOR, "._3JTw7f")
for i in ilanBilgileri:
    print(i.text)

time.sleep(2)

driver.close()

