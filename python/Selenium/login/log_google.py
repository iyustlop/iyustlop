# Google login module

def loggin_google (driver,usuario,password):
	user=driver.find_element_by_id('Email')
	user.clear()
	user.send_keys(usuario)

	next=driver.find_element_by_id('next')
	next.click()

	driver.implicitly_wait(20) #//gives an implicit wait for 20 seconds

	contrasena=driver.find_element_by_id('Passwd')
	#contrasena.clear()
	contrasena.send_keys(password)

	next=driver.find_element_by_id('signIn')
	next.click()
