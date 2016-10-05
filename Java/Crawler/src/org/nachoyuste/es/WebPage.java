package org.nachoyuste.es;

import java.io.IOException;
import java.sql.Timestamp;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class WebPage {
	
	private Anchor anchor;
	private String webPageHash;
	private int anchorParseStatus;
	private int emailParseStatus;
	
	private Document document;
	
	public WebPage(Anchor anchor) {
		super();
		this.anchor = anchor;
	}
	
	private void loadDocumentFromWeb(){
		
		try {
			document = Jsoup.connect(anchor.getAnchorURL()).get();
				
		} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		}
	}

}
