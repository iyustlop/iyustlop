package org.nachoyuste.com;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class diggReader {
	
	public void landingDiggReader(WebDriver driver) {
		
		WebElement log_in = driver.findElement(By.id("step-to-sign-in"));
		log_in.click();
		
		WebElement google_button = driver.findElement(By.id("btn-google-auth"));
		google_button.click();
		
	}
	
	public void selectJobs(WebDriver driver) throws InterruptedException {
		WebElement my_jobs = driver.findElement(By.xpath("//*[@id=\"root-feed-list\"]/li[6]/div[2]"));
		my_jobs.click();
		
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);

		WebElement my_panel = driver.findElement(By.id("view-region-main-container"));
		my_panel.click();
		
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		my_panel.sendKeys("j");

//		while (true){
//			my_panel.sendKeys("j");
//			TimeUnit.SECONDS.sleep(5);
//		}
		
	}

}
