import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String input = sc.nextLine();
		
		int index = input.indexOf('.');
		if (index == -1) {
			System.out.println(input);
		} else {
			System.out.println(input.substring(0, index));
		}
	}

}
