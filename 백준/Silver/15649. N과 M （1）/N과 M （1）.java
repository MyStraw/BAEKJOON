import java.util.Scanner;

public class Main {

	static int N, M;
	static int[] dfs;
	static boolean[] used;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		N = sc.nextInt();
		M = sc.nextInt();

		dfs = new int[M];
		used = new boolean[N + 1];

		backtrack(0);

	}

	static void backtrack(int count) {
		if (count == M) {
			for (int num : dfs) {
				System.out.print(num + " ");
			}
			System.out.println();
			return;
		}
		for (int i = 1; i <= N; i++) {
			if (!used[i]) {
				used[i] = true;
				dfs[count] = i;
				backtrack(count + 1);
				used[i] = false;
			}
		}
	}

}
