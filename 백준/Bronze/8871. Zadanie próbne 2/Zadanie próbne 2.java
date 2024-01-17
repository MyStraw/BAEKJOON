import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
	
		int min = 2 * n + 2;
		int max = 3 * n + 3;

		System.out.println(min + " " + max);

	}

}
