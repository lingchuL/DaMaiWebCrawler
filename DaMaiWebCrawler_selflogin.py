# -*-coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

import requests
import json
from bs4 import BeautifulSoup
from tqdm import tqdm

from urllib.parse import urljoin

import time

option = webdriver.ChromeOptions()

option.add_argument(r'user-data-dir=C:\Users\PC\AppData\Local\Google\Chrome\User Data backup')
option.add_argument("--disable-gpu")
option.add_argument("--no-sandbox")
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"')
# option.add_argument(r"detach = true")

browser = webdriver.Chrome(options=option)

url = "https://detail.damai.cn/item.htm?spm=a2oeg.home.searchtxt.ditem_1.591b23e1Yu31lk&id=687926742033"
testurl = "https://detail.damai.cn/item.htm?id=687315832580"

browser.get(testurl)

browser.maximize_window()

browser.implicitly_wait(10)

# 选中vip票
# VIPButton = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/div/div[2]/div")
SkuNameButtons = browser.find_elements(By.CLASS_NAME, "skuname")
for button in SkuNameButtons:
	if "228" not in button.text:
		continue
	VIPButton = button
	actions = ActionChains(browser)
	actions.move_to_element(VIPButton)
	actions.click()
	actions.perform()

# 点击购买
BuyButton = browser.find_element(By.CLASS_NAME, "buybtn")
actions = ActionChains(browser)
actions.move_to_element(BuyButton)
actions.click()
actions.perform()

# 点击确认
ConfirmButton = browser.find_element(By.CLASS_NAME, "next-btn next-btn-normal next-btn-medium")
actions = ActionChains(browser)
actions.move_to_element(ConfirmButton)
actions.click()
actions.perform()

time.sleep(30)
browser.quit()

