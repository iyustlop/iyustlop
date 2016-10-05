package org.nachoyuste.com;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class chrome_diggReader {

	public static void main(String[] args) throws InterruptedException {
		System.setProperty("webdriver.chrome.driver", "/home/portatil/Documentos/Desarrollo/Java/Librerias/chromedriver");
		
		WebDriver driver = new ChromeDriver();
		
		driver.get("http://www.digg.com/reader");
		driver.manage().window().maximize();
		
		diggReader my_diggReader = new diggReader();
		my_diggReader.landingDiggReader(driver);
		
		logGoogle my_logGoogle = new logGoogle();
		my_logGoogle.logInGoogle(driver,"iyustlop@gmail.com","Borealis");
		
		my_diggReader.selectJobs(driver);

	}

}
