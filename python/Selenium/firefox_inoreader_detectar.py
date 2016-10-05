#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from log_google import loggin_google
from inoreader import landingInInoreader
import time
import sys

driver = webdriver.Firefox()
driver.maximize_window() 

#voy a Inoreader y pincho el enlace 
landingInInoreader(driver)

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

#me logueo en google.
loggin_google (driver,"iyustlop@gmail.com","password")

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

panel = driver.find_element_by_id('feed_searcher')
panel.send_keys(str(sys.argv[3]))
#driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds
panel.send_keys(Keys.RETURN)

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

#Selecciono mis articulos 
my_articles=driver.find_element_by_xpath('//*[@id="reader_pane"]/div[1]/div[1]/div[1]')
my_articles.click()

#Pincho en el panel
lectura = driver.find_element_by_id('reader_pane')
lectura.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

my_feeds = driver.find_element_by_xpath('//*[@id="sb_rp_heading"]/a').text

if (my_feeds == 'Found 0 articles'):
	print ('error_10: No hay articulos')
	driver.close()
else:
	while True:
		lectura.send_keys("j")
		#fecha = driver.find_element_by_class_name('header_date').text
		#print(fecha)
		time.sleep(float(sys.argv[1]))







