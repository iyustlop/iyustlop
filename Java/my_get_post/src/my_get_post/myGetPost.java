package my_get_post;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.net.CookieHandler;
import java.net.CookieManager;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javax.net.ssl.HttpsURLConnection;

public class myGetPost {
	
	private List<String> my_cookies;
	private HttpsURLConnection my_conn;
	
	private final String MY_USER_AGENT = "Mozilla/5.0";

	public static void main(String[] args) throws Exception{
		
		//declaro las URL
		String url = "https://www.theoldreader.com";
//		String url = "https://accounts.google.com/ServiceLoginAuth";
		String gmail = "https://mail.google.com/mail/";
		
		//  Creo una nueva instancia de mi clase, entiendo que para tener todos los metodos que he creado.
		myGetPost http = new myGetPost();
		
		// gestor de las cookie.
		CookieHandler.setDefault(new CookieManager());
		
		String page = http.GetPageContent(url);
		String postParams = http.getFormParams(page, "iyustlop@gmail.com", "Borealis");
		
		// 2. Construct above post's content and then send a POST request for
		// authentication
		http.sendPost(url, postParams);

		// 3. success then go to gmail.
		String result = http.GetPageContent(gmail);
		System.out.println(result);
		
	}
	
	private String GetPageContent(String url) throws Exception{
		
		// Me creo un objeto URL Que es el que voy a conectar
		URL my_obj = new URL(url);
		my_conn = (HttpsURLConnection) my_obj.openConnection();
		
		// Elijo el metodo de conexion. En este caso "GET" por que voy a traerme cosas.
		my_conn.setRequestMethod("GET");
		my_conn.setUseCaches(false);
		
		// act lika a browser
		my_conn.setRequestProperty("User-Agent", MY_USER_AGENT);
		my_conn.setRequestProperty("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
		my_conn.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
		if (my_cookies != null) {
			for (String cookie : this.my_cookies) {
				my_conn.addRequestProperty("Cookie", cookie.split(";", 1)[0]);
			}
		}
		
		int my_responseCode = my_conn.getResponseCode();
		System.out.println("\nSending 'GET' request to URL : " + url);
		System.out.println("Response Code : " + my_responseCode);

		BufferedReader my_in = 
	            new BufferedReader(new InputStreamReader(my_conn.getInputStream()));
		String my_inputLine;
		StringBuffer my_response = new StringBuffer();

		while ((my_inputLine = my_in.readLine()) != null) {
			my_response.append(my_inputLine);
			System.out.println(my_inputLine);
		}
		my_in.close();

		// Get the response cookies
		setCookies(my_conn.getHeaderFields().get("Set-Cookie"));

		return my_response.toString();
		
	}
	
	public String getFormParams(String html, String username, String password) throws UnsupportedEncodingException {

	System.out.println("Extracting form's data...");

	Document doc = Jsoup.parse(html);

	// Google form id
	Element loginform = doc.getElementById("gaia_loginform");
	Elements inputElements = loginform.getElementsByTag("input");
	List<String> paramList = new ArrayList<String>();
	for (Element inputElement : inputElements) {
		String key = inputElement.attr("name");
		String value = inputElement.attr("value");

		if (key.equals("Email"))
			value = username;
		else if (key.equals("Passwd"))
			value = password;
		paramList.add(key + "=" + URLEncoder.encode(value, "UTF-8"));
	}
	
	// build parameters list
	StringBuilder result = new StringBuilder();
	for (String param : paramList) {
		if (result.length() == 0) {
			result.append(param);
		} else {
			result.append("&" + param);
		}
	}
	
	return result.toString();
	
	}
	
	private void sendPost(String url, String postParams) throws Exception {

	URL obj = new URL(url);
	my_conn = (HttpsURLConnection) obj.openConnection();

	// Acts like a browser
	my_conn.setUseCaches(false);
	my_conn.setRequestMethod("POST");
	my_conn.setRequestProperty("Host", "accounts.google.com");
	my_conn.setRequestProperty("User-Agent", MY_USER_AGENT);
	my_conn.setRequestProperty("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8");
	my_conn.setRequestProperty("Accept-Language", "en-US,en;q=0.5");
	
	for (String cookie : this.my_cookies) {
		my_conn.addRequestProperty("Cookie", cookie.split(";", 1)[0]);
	}
	
	my_conn.setRequestProperty("Connection", "keep-alive");
	my_conn.setRequestProperty("Referer", "https://accounts.google.com/ServiceLoginAuth");
	my_conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
	my_conn.setRequestProperty("Content-Length", Integer.toString(postParams.length()));

	my_conn.setDoOutput(true);
	my_conn.setDoInput(true);

	// Send post request
	DataOutputStream wr = new DataOutputStream(my_conn.getOutputStream());
	wr.writeBytes(postParams);
	wr.flush();
	wr.close();

	int responseCode = my_conn.getResponseCode();
	System.out.println("\nSending 'POST' request to URL : " + url);
	System.out.println("Post parameters : " + postParams);
	System.out.println("Response Code : " + responseCode);

	BufferedReader in =  new BufferedReader(new InputStreamReader(my_conn.getInputStream()));
	String inputLine;
	StringBuffer response = new StringBuffer();

	while ((inputLine = in.readLine()) != null) {
		response.append(inputLine);
	}
	in.close();
	// System.out.println(response.toString());

	}
	
	public List<String> getCookies() {
		return my_cookies;
	}

	public void setCookies(List<String> cookies) {
	this.my_cookies = cookies;
	}

}
