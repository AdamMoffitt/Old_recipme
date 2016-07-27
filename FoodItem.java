/**
 * 
 */

/**
 * @author Adam Moffitt
 *
 */
public class FoodItem {


	public String name;
	public int daysPerishable;
	public int quantity;
	public double unitPrice;
	public int priority;
	public String unitSize;
	
	/*
	 * Base Constructor
	 */
	public FoodItem(){
		this.name = null;
		this.daysPerishable = 0;
		this.quantity = 0;
		this.unitPrice = 0;
		this.priority = 0;
	}
	
	/*
	 * Constructor 1
	 */
	public FoodItem(String name) {
		this();
		this.name = name;
	}
	
	/*
	 * Constructor 2
	 */
	public FoodItem(String name, int quantity){
		this(name);
		this.quantity = quantity;
	}

	/*
	 * Constructor 3
	 */
	public FoodItem(String name, int daysPerishable, int quantity, String unitSize, double unitPrice, int priority) {
		super();
		this.name = name;
		this.daysPerishable = daysPerishable;
		this.quantity = quantity;
		this.unitSize = unitSize;
		this.unitPrice = unitPrice;
		this.priority = priority;
	}

	
	
	@Override
	public String toString() {
		return "\n\tName: " + name + 
				"\n\t Good for " + daysPerishable + 
				" days \n\t Quantity: " + quantity + 
				"\n\t Price= $" + unitPrice + 
				"\n\t Priority= " + priority + "\n";
	}
	
}
