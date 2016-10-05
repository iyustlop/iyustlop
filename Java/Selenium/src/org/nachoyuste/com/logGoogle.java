package org.nachoyuste.com;

import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;

public class logGoogle {
	
	public void logInGoogle(WebDriver driver, String usuario, String password) {
		
		
		WebElement my_usuario = driver.findElement(By.id("Email"));
		my_usuario.sendKeys(usuario);
		
		WebElement boton_siguiente = driver.findElement(By.id("next"));
		boton_siguiente.click();
		
		driver.manage().timeouts().implicitlyWait(10, TimeUnit.SECONDS);
		
		WebElement my_passwd = driver.findElement(By.id("Passwd"));
		my_passwd.sendKeys(password);
		
		WebElement boton_iniciar_sesion = driver.findElement(By.id("signIn"));
		boton_iniciar_sesion.click();
		
	}

}
