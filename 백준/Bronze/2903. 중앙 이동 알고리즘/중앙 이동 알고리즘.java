import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int n = (int) Math.pow(2, N) + 1;
		System.out.println((int)Math.pow(n, 2));
	}
}