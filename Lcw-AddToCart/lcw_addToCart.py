import os
from selenium.webdriver.common.keys import Keys

from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains


user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/117.0'
firefox_driver = os.path.join(os.getcwd(), 'geckodriver.exe')
firefox_service = Service(firefox_driver)
firefox_options = Options()
firefox_options.set_preference('general.useragent.override', user_agent)


service= Service(executable_path="geckodriver.exe")
driver = webdriver.Firefox(service=service)
driver.get('https://www.lcwaikiki.com/tr-TR/TR')


home_page_link = 'https://www.lcwaikiki.com/tr-TR/TR'
category_element_locator = ".menu-nav__lists > li:nth-child(1) > a"
subcategory_element_locator = ".menu-header-item--active .zone-item:nth-child(38) > a"
product_locator = "div.product-list .product-card:nth-child(1) > a"
add_to_cart_Locator = "#pd_add_to_cart"
cart_page_locator =  "#header__container > header > div.header__middle > div.header__middle__right > div > div:nth-child(3) > div:nth-child(3) > div > div.cart-action > a"

driver.maximize_window()
time.sleep(2)

def click(locator_value):
     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,locator_value))).click()
    
def goToHomePage():
    #Open main page
    driver.get(home_page_link)
    assert home_page_link == driver.current_url, "Sayfa doğru değil."

def goToCategoryPage():
    #Open Category Page
    categoryElement = WebDriverWait(driver, 100).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,category_element_locator)))
    hover = ActionChains(driver).move_to_element(categoryElement)
    hover.perform()
    
    click(subcategory_element_locator)
    time.sleep(2)

    assert driver.current_url.find("etiket") > -1 or driver.current_url.find("kategori") > -1

def scrollToProduct():
    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return 300")
    driver.execute_script("window.scrollTo(0,300);")
    time.sleep(1)

def goToProductPage():
    #Open product page
    product = click(product_locator)
    time.sleep(1)

    assert driver.current_url.find("urun") > -1, "This page is not the product page."

def addToCart():
    #Add to Card
    click(add_to_cart_Locator)
    print("LOG: The product has been successfully added to the cart.")

def goToCartPage():
    #Open Card Page
    click(cart_page_locator)

    time.sleep(2)

    assert len(driver.find_elements(By.CSS_SELECTOR,'.seller-products-area')) > 0 , "There are no items in the cart!"

def setup():
    goToHomePage()
    goToCategoryPage()
    scrollToProduct()
    goToProductPage()
    addToCart()
    goToCartPage()
    time.sleep(5)
    driver.close()

setup()




