# Zahra Jiriaei 9830065
# Image search


print("welcome to bing!")

# Import Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Make a browser
driver = webdriver.Chrome('chromedriver.exe')

#Goto Bing
driver.get('https://www.bing.com/')

# Select Image
Image_button = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[3]/header/div[1]/div/ul/li[1]/a')))
Image_button.click()


# Serching image
def Image_search():
    # Input text to search
    SearchImage=str(input("What do you want to search?"))
    #inputting text into a box
    box = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/header/form/div/input[1]')))
    print(box)
    box.send_keys(SearchImage)
    box.send_keys(Keys.ENTER)

    # Showing Image Link
    ## Go to the web page
    Current_url=str(driver.current_url)
    page = requests.get(Current_url)

    ## Make soup!
    soup = BeautifulSoup(page.text, 'html.parser')

    ## Finding all photoes
    Photos = soup.find_all('img', {'class' : 'mimg rms_img'})
    for link in Photos:
        print(link.get('src'))
        
    Decision=str(input("Do you want to:\n (1) serch again\n (2) Show more\n (3) Exit\n"))
    return(Decision)

if Image_search()==2:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(5) 
    Photos = soup.find_all('img', {'class' : 'mimg rms_img'})
    for link in Photos:
        print(link.get('src'))


elif Image_search()==1:
    box = WebDriverWait(driver,5).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/header/form/div/input[1]')))
    box.sendKeys(Keys.CONTROL,"a")
    box.sendKeys(Keys.BACKSPACE)
    box.clear()
    Image_search()
        
else:
    print("Goodbye")
Image_search()
        
    

      
