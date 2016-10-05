from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import sys

driver=webdriver.Chrome('/home/sobremesa/Descargas/chromedriver')
driver.maximize_window() #

driver.get("http://www.inoreader.com")

link=driver.find_element_by_id('login_air')
NewWindow=link.click()

title=driver.find_element_by_xpath('//*[@id="landing_signin_form"]/div[3]/div[2]/button[2]')
title.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

user=driver.find_element_by_id('Email')
user.clear()
user.send_keys("iyustlop@gmail.com")

next=driver.find_element_by_id('next')
next.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

password=driver.find_element_by_id('Passwd')
#password.clear()
password.send_keys("Password")

next=driver.find_element_by_id('signIn')
next.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

panel = driver.find_element_by_id('feed_searcher')
panel.send_keys(str(sys.argv[2]))
panel.send_keys(Keys.RETURN)

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

my_articles=driver.find_element_by_xpath('//*[@id="reader_pane"]/div[1]/div[1]/div[1]')
my_articles.click()

lectura = driver.find_element_by_id('reader_pane')
lectura.click()

while True:
	lectura.send_keys("j")
	time.sleep(float(sys.argv[1]))






