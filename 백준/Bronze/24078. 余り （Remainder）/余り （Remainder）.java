import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);		
		int X = sc.nextInt();		
		int remainder = X % 21;	
		System.out.println(remainder);
	}
}