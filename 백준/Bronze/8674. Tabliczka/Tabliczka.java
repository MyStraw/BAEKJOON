import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long a = sc.nextLong();
		long b = sc.nextLong();		

		long ver = (b % 2 == 0) ? 0 : a;

		long hor = (a % 2 == 0) ? 0 : b;

		System.out.println(Math.min(ver, hor));
	}

}
