import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[][] Z;
	static int count = -1;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		System.out.println(Z재귀(n, r, c));
	}

	static int Z재귀(int n, int x, int y) {
		if (n == 0) {
			return 0;
		}

		int half = 1 << (n - 1);

		if (x < half && y < half) {
			return Z재귀(n - 1, x, y);
		} else if (x < half && y >= half) {
			return half * half + Z재귀(n - 1, x, y - half);
		} else if (x >= half && y < half) {
			return 2 * half * half + Z재귀(n - 1, x - half, y);
		} else {
			return 3 * half * half + Z재귀(n - 1, x - half, y - half);
		}
	}
}
