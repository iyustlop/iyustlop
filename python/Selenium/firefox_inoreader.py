#!/usr/bin/env python

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
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

#panel = driver.find_element_by_id('link_0_1852145')
panel = driver.find_element_by_id('link_0_2940220')
panel.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

lectura = driver.find_element_by_id('reader_pane')
lectura.click()

while True:
	lectura.send_keys("j")

	#contador = driver.find_element_by_id('unread_cnt_0_1852145').text
	contador = driver.find_element_by_id('unread_cnt_0_2940220').text
	#if (contador == '999'):
	print(contador)

	time.sleep( float(sys.argv[1]) )







