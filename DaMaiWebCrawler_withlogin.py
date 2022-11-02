# -*-coding:utf-8 -*-
import os.path

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
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_argument(
	r'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"')
# option.add_argument(r"detach = true")
option.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome(options=option)

browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
	"source": """
		Object.defineProperty(navigator, 'webdriver', {
			get: () => undefined
		})
		"""
})

url = "https://detail.damai.cn/item.htm?id=691288119897"
testurl = "https://detail.damai.cn/item.htm?id=687315832580"

browser.get(testurl)

browser.maximize_window()

browser.implicitly_wait(15)

if os.path.exists(r"E:\\damai_cookies.txt"):
	# 如果有cookies 直接登录

	with open(r"E:\\damai_cookies.txt", "r", encoding="utf-8") as f:
		listCookies = json.loads(f.read())

	for cookie in listCookies:
		cookie_dict = {
			'domain': '.damai.cn',
			'name': cookie.get('name'),
			'value': cookie.get('value'),
			'expires': '',
			'path': '/',
			'httpOnly': False,
			'HostOnly': False,
			'Secure': False
		}
		browser.add_cookie(cookie_dict)
	browser.refresh()
else:
	# 点击登录

	ToLoginButton = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div[1]")
	# ToLoginButton = browser.find_element(By.CLASS_NAME, "login-user show")
	actions = ActionChains(browser)
	actions.move_to_element(ToLoginButton)
	actions.click()
	actions.perform()

# 检验是否跳转到了详情页面

WebDriverWait(browser, 30, 0.1).until(
	EC.title_contains("【广州】")
)

print("成功登录")

dictCookies = browser.get_cookies()
jsonCookies = json.dumps(dictCookies)

with open(r"E:\\damai_cookies.txt", "w") as f:
	f.write(jsonCookies)

# 等待到时间


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

# 通过购买按钮判断是否刷新
bHasRefresh = False
while True:
	BuyButton = browser.find_elements(By.CLASS_NAME, "buybtn")
	for button in BuyButton:
		if "购买" in button.text:
			bHasRefresh = True
			break

	if bHasRefresh:
		break

time.sleep(0.1)

# 检查登陆状态
bHasRefreshLogin = False
while True:
	UserNames = browser.find_elements(By.CLASS_NAME, "name-user")
	for username in UserNames:
		if "麦子41xL2" not in username.text:
			time.sleep(0.001)
		else:
			bHasRefreshLogin = True
			print("购买页面刷新后已成功再次登录！")
			break

	if bHasRefreshLogin:
		break

# 点击购买
bHasClickedBuy = False
while True:
	BuyButton = browser.find_elements(By.CLASS_NAME, "buybtn")
	for button in BuyButton:
		if "购买" in button.text:
			realBuyButton = button

			actions = ActionChains(browser)
			actions.move_to_element(realBuyButton)
			actions.click()
			actions.perform()

			print("已点击BuyBtn")
			bHasClickedBuy = True

	if bHasClickedBuy:
		break
	else:
		time.sleep(0.00001)

# 点击确认

bHasFoundConfirmButton = False
while True:
	ConfirmButtons = browser.find_elements(By.CLASS_NAME, "next-btn")
	for button in ConfirmButtons:
		if "提交订单" in button.text:
			bHasFoundConfirmButton = True
			RealConfirmButton = button

			actions = ActionChains(browser)
			actions.move_to_element(RealConfirmButton)
			actions.click()
			actions.perform()

			break

	if bHasFoundConfirmButton:
		break


time.sleep(60)
browser.quit()
