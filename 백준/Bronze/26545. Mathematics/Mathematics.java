import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int total = 0;

		for (int i = 0; i < N; i++) {
			int plus = sc.nextInt();
			total += plus;
		}
		
		System.out.println(total);
	}

}
