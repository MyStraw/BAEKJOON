import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int p1 = Integer.parseInt(st.nextToken());
		int q1 = Integer.parseInt(st.nextToken());
		int p2 = Integer.parseInt(st.nextToken());
		int q2 = Integer.parseInt(st.nextToken());

		long numerator = (long) p1 * p2;
		long denominator = 2L * q1 * q2;

		if (numerator % denominator == 0) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}
	}

}
