package org.nachoyuste.es;

import java.sql.Timestamp;

public class Anchor {
	private Domain domain;
	private String AnchorHash;
	private String AnchorURL;
	private int scanStatus;
	private boolean activated;
	private Timestamp modified;
	private Timestamp created;
	public Domain getDomain() {
		return domain;
	}
	public void setDomain(Domain domain) {
		this.domain = domain;
	}
	public String getAnchorHash() {
		return AnchorHash;
	}
	public void setAnchorHash(String anchorHash) {
		AnchorHash = anchorHash;
	}
	public String getAnchorURL() {
		return AnchorURL;
	}
	public void setAnchorURL(String anchorURL) {
		AnchorURL = anchorURL;
	}
	public int getScanStatus() {
		return scanStatus;
	}
	public void setScanStatus(int scanStatus) {
		this.scanStatus = scanStatus;
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
	public Anchor(Domain domain, String anchorHash, String anchorURL) {
		super();
		this.domain = domain;
		AnchorHash = anchorHash;
		AnchorURL = anchorURL;
	}
	public Anchor(Domain domain, String anchorHash, String anchorURL, int scanStatus, boolean activated,
			Timestamp modified, Timestamp created) {
		super();
		this.domain = domain;
		AnchorHash = anchorHash;
		AnchorURL = anchorURL;
		this.scanStatus = scanStatus;
		this.activated = activated;
		this.modified = modified;
		this.created = created;
	}
	
	

}
