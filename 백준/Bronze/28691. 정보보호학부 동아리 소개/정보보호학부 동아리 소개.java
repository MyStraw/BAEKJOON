import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner (System.in);		
		String N = sc.next();			
		
		if ( N.equals("M"))
			System.out.println("MatKor");
		if ( N.equals("W"))
			System.out.println("WiCys");
		if ( N.equals("C"))
			System.out.println("CyKor");
		if ( N.equals("A"))
			System.out.println("AlKor");
		if ( N.equals("$"))
			System.out.println("$clear");		
		
	}

}
