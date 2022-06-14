from selenium import webdriver
import requests 
from bs4 import BeautifulSoup as bs 
from selenium.webdriver.common.keys import Keys
import time 
import random


with open('messages.txt', 'r', encoding = 'utf-8') as messages:
    messagelist = list()
    text = messages.read()
    messagelist = text.split('\n')

print(messagelist)
