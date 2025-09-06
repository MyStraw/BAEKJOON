import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner scn = new Scanner(System.in);

		int h = scn.nextInt();
		int m = scn.nextInt();

		if (0 <= h && h <= 23 && 0 <= m && m <= 59) {
			if (h == 0 && m < 45) {
				h = 23;
				m = 60 - (45 - m);
				System.out.print(h + " " + m);

			} else if (h >= 1 && m < 45) {
				h = h - 1;
				m = 60 - (45 - m);
				System.out.print(h + " " + m);

			} else {
				m = m - 45;
				System.out.print(h + " " + m);

			}

		}

	}
}