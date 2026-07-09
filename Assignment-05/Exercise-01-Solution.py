# Zahra Jiriaei 98471189
# Boston Jobs



# Import webdriver for browsing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

# Welcome massage
print("Welcom to Boston Jobs offer /n we will help you to find a job")

# Make a browser
driver = webdriver.Chrome('chromedriver.exe')

# Go to the web page
driver.get('https://boston.craigslist.org/search/jjj?')

# Click on jobs
Jobs = driver.find_element_by_xpath('/html/body/section/header[1]/nav/form/ul/li[4]/select')
Jobs.click()

# Choosing job group
print("Choose one number from list below")

# Finding list of jobs name

## Go to the web page
page = requests.get('https://boston.craigslist.org/search/jjj?')

## Make soup!
soup = BeautifulSoup(page.text, 'html.parser')

## Finding all names
Jobs = soup.find_all('select', {'class' : 'js-only'})

## Put a names in the list
Job_list=[]
for JobGroup in Jobs:
    Job_list.append(JobGroup.text)
Job_list=Job_list[1].split("\n")
del Job_list[0]
del Job_list[-1]

# Show jobs Group name
for name in Job_list:
    print(f"({Job_list.index(name)+1}) {name}")

# input the number
Number=int(input("Enter the number"))

# Go to the job group webpage
Xpath=f"/html/body/section/header[1]/nav/form/ul/li[4]/select/option[{Number}]"
Job_Group = driver.find_element_by_xpath(Xpath)
Job_Group.click()
print(Job_Group.text)
# Printing Jobs title
Job_titles = soup.find_all('h3', {'class' : 'result-heading'})
titles=[]
for JobTitles in Job_titles:
    titles.append(JobTitles.text)
for titlename in range(0,len(titles),3):
    print(f"({titlename+1})   {titles[titlename]}")

# Show web page

chooshen_job=int(input('Enter the number of the job title'))
Xpath=f"/html/body/section/form/div[4]/ul/li[{chooshen_job}]/div/h3/a"
Job_Title = driver.find_element_by_xpath(Xpath)
Job_Title.click()

