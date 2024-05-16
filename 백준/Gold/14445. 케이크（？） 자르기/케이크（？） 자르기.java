import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		long n = Long.parseLong(br.readLine());
		long result;
		if (n > 1) {
			result = (n + 1) / 2;
		} else
			result = 0;
		System.out.println(result);
	}
}