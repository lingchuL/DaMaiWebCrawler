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

option.add_argument(r"user-data-dir=C:\Users\PC\AppData\Local\Google\Chrome\User Data_backup")
# option.add_argument(r"detach = true")

browser = webdriver.Chrome(options=option)

url = "https://detail.damai.cn/item.htm?spm=a2oeg.home.searchtxt.ditem_1.591b23e1Yu31lk&id=687926742033"

LoginPhoneNumber = "17611252331"
Password = "Tiruey520"

browser.get(url)

browser.maximize_window()

browser.implicitly_wait(10)

# 点击登录

ToLoginButton = browser.find_element(By.XPATH, "/html/body/div[2]/div/div[3]/div[1]/div[1]/span")
# ToLoginButton = browser.find_element(By.CLASS_NAME, "login-user show")
actions = ActionChains(browser)
actions.move_to_element(ToLoginButton)
actions.click()
actions.perform()


# LoginPhoneTextInput = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[1]/div[2]/input")
# LoginPhoneTextInput = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[1]/div[2]")
LoginPhoneTextInput = browser.find_elements(By.NAME, "fm-login-id")
print(LoginPhoneTextInput)
for InputUI in LoginPhoneTextInput:
	actions = ActionChains(browser)
	actions.move_to_element(LoginPhoneTextInput)
	actions.click()
	actions.send_keys(LoginPhoneNumber)
	actions.perform()


PasswordTextInput = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[2]/div[2]")
# PasswordTextInput = browser.find_element(By.ID, "fm-login-password")
actions = ActionChains(browser)
actions.move_to_element(PasswordTextInput)
actions.click()
actions.send_keys(Password)
actions.perform()


# LoginButton = browser.find_element_by_xpath("/html/body/div/div/div[2]/div/form/div[4]/button")
LoginButton = browser.find_element(By.XPATH, "/html/body/div/div/div[2]/div/form/div[4]/button")
# LoginButton = browser.find_element(By.CLASS_NAME, "fm-button fm-submit password-login")
actions = ActionChains(browser)
actions.move_to_element(LoginButton)
actions.click()
actions.perform()


# 检验是否跳转到了详情页面


# 选中vip票
# VIPButton = browser.find_element_by_xpath("/html/body/div[3]/div/div[1]/div[1]/div/div[2]/div[3]/div[6]/div[2]/div/div[2]/div")
SkuNameButtons = browser.find_elements(By.CLASS_NAME, "skuname")
for button in SkuNameButtons:
	if "VIP350" not in button.text:
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

