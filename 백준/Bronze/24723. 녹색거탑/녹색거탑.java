import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		if (N == 1) {
			System.out.println(2);
		} else if (N == 2) {
			System.out.println(4);
		} else if (N == 3) {
			System.out.println(8);
		} else if (N == 4) {
			System.out.println(16);
		} else if (N == 5) {
			System.out.println(32);
		}
	}
}
