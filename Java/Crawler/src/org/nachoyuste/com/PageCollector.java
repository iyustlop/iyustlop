package org.nachoyuste.com;

import java.io.IOException;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class PageCollector {
	
	public static void main(String[] args) {	
			
		try {
			Document doc = Jsoup.connect("http://www.kawasakipartshouse.com/oemparts/#/c/kawasaki_motorcycle/parts/").get();
			Elements my_links = doc.select("a");
			for (Element e : my_links){
				System.out.println(e.attr("abs:href"));
			}
				
		} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		}
	}

}
