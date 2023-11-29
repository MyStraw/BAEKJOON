import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		double t = sc.nextInt();
		
		double result = t/5;
		
		System.out.println((int)Math.ceil(result));
		
	}

}
