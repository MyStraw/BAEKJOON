import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		float a = sc.nextFloat();
		float b = sc.nextFloat();		
		
		float c = a*b/2;
		
//		String result = String.format("%.1f", c);
//		System.out.println(result);
		
		System.out.printf("%.1f", c);
	}

}
