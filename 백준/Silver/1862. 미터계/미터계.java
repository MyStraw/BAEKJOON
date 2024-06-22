import java.util.Scanner;

public class Main {
	public static void main(String[] args) {//9진수?
		Scanner sc = new Scanner(System.in);

		int m = sc.nextInt();

		int real = 0;
		int nine = 1;

		while (m > 0) {
			int digit = m % 10;
			m /= 10;

			if (digit > 4) {
				digit -= 1;
			}

			real += digit * nine;
			nine *= 9;

		}

		System.out.println(real);

	}

}
