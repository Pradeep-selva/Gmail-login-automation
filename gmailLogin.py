
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


email = ""
passwd = ""
path=""

with open("credentials.json") as f:
  
    d=json.load(f)
    email=d["email"]
    passwd=d["password"]
    path=d["path"]


driver = webdriver.Chrome(executable_path=path)
driver.get("http://www.gmail.com")
driver.implicitly_wait(15)


username=driver.find_element_by_id("identifierId")
username.send_keys(email)
time.sleep(2)
next=driver.find_element_by_id("identifierNext")
next.click()
time.sleep(3)
password=driver.find_element_by_name("password")
password.send_keys(passwd)
time.sleep(3)
login=driver.find_element_by_id("passwordNext")
login.click()

