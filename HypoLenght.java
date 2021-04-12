// calculation of the length of the hypotenuse in a triangle
import java.util.Scanner;

public class HypoLenght {
	public static void main(String []args) {
		Scanner cathet = new Scanner(System.in);  // Create a Scanner object
		
	    System.out.print("Enter value of first cathet: ");
	    double x = cathet.nextDouble();  // Read user input
	    
	    System.out.print("Enter value of second cathet: ");
	    double y = cathet.nextDouble();  // Read user input
	    double z;//Create a hypotenuse variable
	    
	    z = Math.sqrt(x * x + y *y);
	    System.out.println();
	    System.out.println("Hypotenuse length is: " + z);
	}

}