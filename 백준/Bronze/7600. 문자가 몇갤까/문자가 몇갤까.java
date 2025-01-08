import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String line;

		while (!(line = br.readLine()).equals("#")) {
			HashSet<Character> alphabetSet = new HashSet<>();
			for (char c : line.toLowerCase().toCharArray()) {
				if (c >= 'a' && c <= 'z') {
					alphabetSet.add(c);
				}
			}
			System.out.println(alphabetSet.size());
		}

	}

}
