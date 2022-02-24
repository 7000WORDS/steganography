#Meant to open a text file which 
#will then download a file from the internet and will be only accessible to those who have a special key to access it. 
# we start by importing selenium so that we know when we finish downloading the files. 

from selenium import webdriver
from selenium.webdrive.common.by import By 
from selenium.webdriver.common.keys import Keys


browser = webdriver.chrome()
browser.get("https://nike.com")
assert "nike" in browser.title

elem = browser.find_element(By.Name, 'p')
elem.send_keys('nikehq'+ keys.RETURN)
