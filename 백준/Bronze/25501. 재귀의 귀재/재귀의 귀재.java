import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	static int count;

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());

		for (int i = 0; i < N; i++) {
			count = 0;
			String str = br.readLine();
			char s[] = str.toCharArray();
			bw.write(isPalindrome(s) + " " + count + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}

	public static int recursion(char[] s, int l, int r) {
		if (l >= r) {
			return 1;
		} else if (s[l] != s[r]) {
			return 0;
		} else {
			count++;
			return recursion(s, l + 1, r - 1);
		}
	}

	public static int isPalindrome(char[] s) {
		count++;
		return recursion(s, 0, s.length - 1);
	}

}
