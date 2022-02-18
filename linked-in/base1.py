from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests
  
# Creating a webdriver instance
driver = webdriver.Chrome("E:\webscrapping files\chromedriver_win32\chromedriver.exe")
# This instance will be used to log into LinkedIn
  
# Opening linkedIn's login page
driver.get("https://www.linkedin.com/jobs/?originalSubdomain=in")
  
# waiting for the page to load
time.sleep(5)

  
# entering username
Search_job_titles = driver.find_element_by_type("search")
  
# In case of an error, try changing the element
# tag used here.
  
# Enter Your Email Address
Search_job_titles.send_keys("chennai")  
    
# entering password
location = driver.find_element_by_type("search")
# In case of an error, try changing the element 
# tag used here.
  
# Enter Your Password
location.send_keys("Chennai, Tamil Nadu, India")        
  
# Clicking on the log in button
# Format (syntax) of writing XPath --> 
# //tagname[@attribute='value']
driver.find_element_by_xpath("//button[@type='submit']").click()
# In case of an error, try changing the5
# XPath used here.

# Opening Kunal's Profile
# paste the URL of Kunal's profile here



profile_url = "https://www.linkedin.com/in/kunalshah1/"
  
driver.get(profile_url)  
