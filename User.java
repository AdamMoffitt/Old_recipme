/*
 * User 
 */
public class User {

	Kitchen myKitchen = new Kitchen();
	String history[]; //History???????
	private double superMarketId;
	
	//info
	public String name;
	private String password;
	private String email;
	int age;
	char gender;
	public Kitchen getMyKitchen() {
		return myKitchen;
	}
	
	public void setMyKitchen(Kitchen myKitchen) {
		this.myKitchen = myKitchen;
	}
	public double getSuperMarketId() {
		return superMarketId;
	}
	public void setSuperMarketId(double superMarketId) {
		this.superMarketId = superMarketId;
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name = name;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
	public String getEmail() {
		return email;
	}
	public void setEmail(String email) {
		this.email = email;
	}
	
	//Preferences
	
	
	
}
