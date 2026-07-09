# Zahra Jiriaei 98300065
# Intract with instagram

# import libraries
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
# Make a browser
driver = webdriver.Chrome('chromedriver.exe')

# Go to a Webpage
driver.get('https://www.instagram.com/')

#inputting username and password and pressing ok
username_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')))
pass_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')))

username_box.send_keys("ZJ_AP")
pass_box.send_keys("13791379")

pass_box.send_keys(Keys.ENTER)

# press not now button
save_info_btn = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/div/button')))
save_info_btn.click()
another_btn =WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')))
another_btn.click()

# Click on profile
Profile= WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH,'/html/body')))
Profile.click()

