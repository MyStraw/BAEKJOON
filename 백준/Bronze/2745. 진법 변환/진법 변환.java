import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);

		String N = sc.next();
		int B = sc.nextInt();
	
		long result = 0;

		for (int i = 0; i < N.length(); i++) {
			int value;
			if (N.charAt(i) >= '0' && N.charAt(i) <= '9') {
				value = N.charAt(i) - '0';

			} else {
				value = N.charAt(i) - 'A' + 10;				
			}			
			result = result * B + value;
		}
		System.out.println(result);
	}
}