import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		double A = sc.nextDouble();
		double B = sc.nextDouble();
		double C = sc.nextDouble();

		int result1 = (int) ((A * B) / C);
		int result2 = (int) ((A / B) * C);

		System.out.println(Math.max(result1, result2));

	}

}
