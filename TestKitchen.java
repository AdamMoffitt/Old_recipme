
public class TestKitchen {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Kitchen myKitchen = new Kitchen();
		FoodItem tomato = new FoodItem("tomato", 10);
		FoodItem doritoes = new FoodItem("Doritoes - Sour Cream and Onion", 200, 50, "Ounces", 1.50, 5);
		FoodItem Guacamole = new FoodItem("Guacamole", 2, 5, "Pounds", 5.99, 1);
		
		
		myKitchen.addItem( tomato);
		myKitchen.addItem(Guacamole);
		myKitchen.addItem(doritoes);
		
		myKitchen.printContents();
	}

}
