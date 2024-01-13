import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		
		String pattern = "WelcomeToSMUPC";
		int patternLength = pattern.length();
	
		int N = scanner.nextInt();
	
		char result = pattern.charAt((N - 1) % patternLength);
	
		System.out.println(result);
	}

}
