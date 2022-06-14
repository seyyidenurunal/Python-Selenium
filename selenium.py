from selenium import webdriver
import time

driver_path = "C:\\Users\pc\Desktop\pip\chromedriver"


browser = webdriver.Chrome(driver_path)


browser.get("https://www.nationalgeographic.com/")


print("Site Başlığı: ", browser.title) #Konsola sitenin başlığını yazar.

browser.refresh() # Sayfayı yeniler.



browser.get("https://www.nationalgeographic.com/travel/article/17-stellar-new-hotels-that-embrace-their-geography")

browser.save_screenshot("C://Users/pc/Desktop/Learning JS/nationalgeographic.png")

print(browser.page_source) #Sayfanın kaynağını verir.

browser.set_window_size(700, 500) #Ekranı istenilen boyuta getirir.

browser.save_screenshot("C://Users/pc/Desktop/nationalgeographicpic.png")

time.sleep(2) #2 sn bekler.

browser.back() #Geri döner


time.sleep(5) #5 sn bekler.

browser.quit() # Tarayıcıyı kapatır.

#browser.close()  # Sekmeyi kapatır.
