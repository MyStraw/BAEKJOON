import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader scn = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter prt = new BufferedWriter(new OutputStreamWriter(System.out));

		int T = Integer.parseInt(scn.readLine());
		int sum = 0;

		if (1 <= T && T <= 1_000_000) {
			for (int i = 1; i <= T; i++) {
				String[] input = scn.readLine().split(" ");
				int A = Integer.parseInt(input[0]);
				int B = Integer.parseInt(input[1]);
				if (1 <= A && A <= 1000 && 1 <= B && B <= 1000) {
					sum = A + B;
					prt.write(sum + "\n");
				}
			}
		}

		scn.close();
		prt.flush();
		prt.close();
	}
}
