import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int appleA = sc.nextInt();
		int orangeA = sc.nextInt();
		int appleB = sc.nextInt();
		int orangeB = sc.nextInt();

		if (appleA + orangeB > appleB + orangeA) {
			System.out.println(appleB + orangeA);
		} else
			System.out.println(appleA + orangeB);
	}

}
