#landing in Inoreader and clicking the signIn

def landingInInoreader(driver):
	driver.get("http://www.inoreader.com")

	link = driver.find_element_by_id('login_air')
	NewWindow = link.click()

	googleButton = driver.find_element_by_xpath('//*[@id="landing_signin_form"]/div[3]/div[2]/button[2]')
	googleButton.click()
