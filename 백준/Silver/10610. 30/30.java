import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String N = br.readLine();

		Integer[] num = new Integer[N.length()];

		for (int i = 0; i < N.length(); i++) {
			num[i] = N.charAt(i) - '0';
		}

		int sum = 0;
		boolean zero = false;

		for (int i = 0; i < N.length(); i++) {
			sum += num[i];
			if (num[i] == 0) {
				zero = true;
			}
		}
		if (sum % 3 == 0 && zero) {
			Arrays.sort(num, (a, b) -> b - a);
			for (int a : num) {
				System.out.print(a);
			}
		}
		else {
			System.out.println(-1);
		}
	}
}
