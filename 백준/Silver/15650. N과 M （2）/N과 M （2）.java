import java.util.Scanner;

public class Main {
	static int N, M;
	static int[] dfs;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		M = sc.nextInt();

		dfs = new int[M];

		backtrack(0, 1);

	}

	static void backtrack(int count, int start) {
		if (count == M) {
			for (int num : dfs) {
				System.out.print(num + " ");
			}
			System.out.println();
			return;
		}
		for (int i = start; i <= N; i++) {
			dfs[count] = i;//
			backtrack(count + 1, i + 1);

		}
	}
}
