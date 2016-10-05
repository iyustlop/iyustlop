from selenium import webdriver
from log_google import loggin_google
from inoreader import landingInInoreader
import time

driver=webdriver.Chrome('/home/portatil/Documentos/Desarrollo/python/Selenium/ChromeDriver/chromedriver')
driver.maximize_window() #

#voy a Inoreader y pincho el enlace 
landingInInoreader(driver)

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

#me logueo en google.
loggin_google (driver,"iyustlop@gmail.com","Password")

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

panel = driver.find_element_by_id('link_0_1545404')
panel.click()

driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

lectura = driver.find_element_by_id('reader_pane')
lectura.click()

while True:
	lectura.send_keys("j")
	time.sleep( 5 )






