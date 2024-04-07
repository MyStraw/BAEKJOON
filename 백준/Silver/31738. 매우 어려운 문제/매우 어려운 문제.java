import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		long N = Long.parseLong(st.nextToken());
		long M = Long.parseLong(st.nextToken());

		if (N >= M) {
			System.out.println(0);
		} else {
			long result = factorial(N, M);
			System.out.println(result);
		}
	}

	public static long factorial(long N, long M) {
		long factorial = 1;
		for (long i = 2; i <= N; i++) {
			factorial = (factorial * i) % M;
		}
		return factorial;
	}
}
