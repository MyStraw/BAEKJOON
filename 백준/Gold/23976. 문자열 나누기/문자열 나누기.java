import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static final int MOD = 1000000007;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		String S = br.readLine();

		long[][][] dp = new long[N + 1][K + 1][2];

		dp[0][0][0] = 1;

		for (int i = 1; i <= N; i++) {
			char c = S.charAt(i - 1);
			for (int j = 1; j <= Math.min(i, K); j++) {
				if (c != '0') {
					dp[i][j][0] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1] + dp[i - 1][j][0]) % MOD;
				} else {
					dp[i][j][0] = dp[i - 1][j][0];
					dp[i][j][1] = (dp[i - 1][j - 1][0] + dp[i - 1][j - 1][1]) % MOD;
				}
			}
		}

		System.out.println((dp[N][K][0] + dp[N][K][1]) % MOD);
	}

}
