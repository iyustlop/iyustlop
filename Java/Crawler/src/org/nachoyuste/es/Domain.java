package org.nachoyuste.es;

import java.sql.Timestamp;

public class Domain {
	private String DomainHash;
	private String DomainURL;
	private boolean activated;
	private Timestamp modified;
	private Timestamp created;
	
	public String getDomainHash() {
		return DomainHash;
	}
	public void setDomainHash(String domainHash) {
		DomainHash = domainHash;
	}
	public String getDomainURL() {
		return DomainURL;
	}
	public void setDomainURL(String domainURL) {
		DomainURL = domainURL;
	}
	public boolean isActivated() {
		return activated;
	}
	public void setActivated(boolean activated) {
		this.activated = activated;
	}
	public Timestamp getModified() {
		return modified;
	}
	public void setModified(Timestamp modified) {
		this.modified = modified;
	}
	public Timestamp getCreated() {
		return created;
	}
	public void setCreated(Timestamp created) {
		this.created = created;
	}
	public Domain(String domainHash, String domainURL) {
		super();
		DomainHash = domainHash;
		DomainURL = domainURL;
	}
	public Domain(String domainHash, String domainURL, boolean activated, Timestamp modified, Timestamp created) {
		super();
		DomainHash = domainHash;
		DomainURL = domainURL;
		this.activated = activated;
		this.modified = modified;
		this.created = created;
	}
	
	

}
