import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int k = sc.nextInt();
		int w = sc.nextInt();
		int m = sc.nextInt();

		int hits = 0;
		while (k < w) {
			k += m;
			hits++;
		}

		System.out.println(hits);

	}

}
