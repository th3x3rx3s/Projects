from encodings import utf_8
from re import I
import requests
from lxml.html import fromstring
from itertools import cycle
import traceback
import urllib.request
from urllib import request as urlrequest
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import main.py
proxy_list=input("Mi a proxy lista file-jának útvonala? ")
f = open(proxy_list,"r")
lista=f.read().splitlines()
f.close()
proxies=iter(lista)
url='https://www.thepetcommunity.com/_pet-photo-contest/entry/0zyb089'

for i in range(len(lista)):
        proxy=next(proxies)
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--proxy-server=%s' % proxy)
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()),options=edge_options)
        print("Request #%d"%i)
        try:
            driver.get(url)
            driver.maximize_window()
            time.sleep(5)
            button = driver.find_element(By.XPATH, "//form[@id='voteEntryForm']/fieldset/div/input")
            button.click()
            driver.quit()
        except:
            print("Skipping.")