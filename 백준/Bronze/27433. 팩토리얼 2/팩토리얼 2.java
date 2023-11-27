import java.util.Scanner;

public class Main {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		long N = sc.nextInt();

		long combi = 1;

		for (int i = 1; i <= N; i++) {
			combi = combi * i;
		}

		System.out.println(combi);
	}

}
