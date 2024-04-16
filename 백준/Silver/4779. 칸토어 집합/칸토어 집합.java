import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input;
		
		while ((input = br.readLine()) != null) {
			if(input.isEmpty()) continue;
			int N = Integer.parseInt(input);
			System.out.println(can((int) Math.pow(3, N)));			
		}		
	}
	public static String can(int length) {
		if (length == 1) {
			return "-";
		} else {
			int partLen = length / 3;
			String part = can(partLen);
			return part + " ".repeat(partLen) + part;
		}
	}
}