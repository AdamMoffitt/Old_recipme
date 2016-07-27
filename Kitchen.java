/**
 * Kitchen class stores the food items that the user owns. Includes addItem function, removeItem function,
 * printContents function,
 */

import java.util.HashMap;

/**
 * @author Adam Moffitt
 *
 */
public class Kitchen {

	HashMap<String, FoodItem> myKitchen;
	
	public Kitchen(){
		myKitchen = new HashMap<String, FoodItem>();
	}

	public void addItem(FoodItem newFood){
		myKitchen.put(newFood.name, newFood);
	}
	
	public void removeItem(String name){
		myKitchen.remove(name);
	}
	
	public void printContents(){
		for(String key: myKitchen.keySet())
			        System.out.println(key + " - " + myKitchen.get(key));
			        System.out.println();
	}
	
	
}
