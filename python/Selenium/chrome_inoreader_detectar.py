#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from login.log_google import loggin_google
from webs.inoreader import landingInInoreader
from user.user import myUser
import time
import sys
import logging

def main():
	logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s')
	usuario = myUser()
	
	logging.info(usuario.getDriver()) 
	driver=webdriver.Chrome(usuario.getDriver())

	if (str(sys.argv[2]) == ''):
		print ('error_2: seleccionar opcion de visualizacion')
		sys.exit()
	elif (str(sys.argv[2]) == 'h'):
		driver.set_window_size(960, 1080)
	elif (str(sys.argv[2]) == 'm'):
		driver.maximize_window()
	else:
		print ('error_1: seleccionar opcion de visualizacion correcta')
		sys.exit()

	#voy a Inoreader y pincho el enlace 
	landingInInoreader(driver)

	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

	#me logueo en google.
	logging.info('%s before you %s', usuario.getUser(), usuario.getPassword())

	loggin_google (driver,usuario.getUser(),usuario.getPassword())

	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

	panel = driver.find_element_by_id('feed_searcher')
	panel.send_keys(str(sys.argv[4]))
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
		logging.error ('error_10: No hay articulos')
		driver.quit()
	else:
		try:
			while True:
				lectura.send_keys("j")
				if (str(sys.argv[3]) == 's'):
					driver.implicitly_wait(10) #//gives an implicit wait for 20 seconds
				else:
					driver.implicitly_wait(1) #//gives an implicit wait for 20 seconds
				#fecha = driver.find_element_by_class_name('header_date').text
				#print(fecha)
				time.sleep(float(sys.argv[1]))
		except Exception as e:
			logging.error ('force close the browser')
			driver.quit()
			sys.exit()

if __name__ == '__main__':
    main()





