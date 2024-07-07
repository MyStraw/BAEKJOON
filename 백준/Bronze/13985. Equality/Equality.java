import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String input = sc.nextLine();
		
		String[] plus = input.split(" ");
	
		int a = Integer.parseInt(plus[0]);
		int b = Integer.parseInt(plus[2]);
		int c = Integer.parseInt(plus[4]);
	
		if (a + b == c) {
			System.out.println("YES");
		} else {
			System.out.println("NO");
		}		

	}

}
