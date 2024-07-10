import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		double a = sc.nextInt();
		double b = sc.nextInt();

		double damage = a - (a * b / 100);

		if (damage < 100) {
			System.out.println(1);
		} else
			System.out.println(0);
	}

}
