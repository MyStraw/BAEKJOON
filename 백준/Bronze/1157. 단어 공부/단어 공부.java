import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;

public class Main {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine().toUpperCase();

		Map<String, Integer> moonjang = new HashMap<>();

		for (int i = 0; i < s.length(); i++) {
			String dan = s.substring(i, i + 1); 
			moonjang.put(dan, moonjang.getOrDefault(dan, 0) + 1);			
		}

		int max = 0;
		String maxDan ="";
		boolean joongbok = false;

		for (Map.Entry<String, Integer> entry : moonjang.entrySet()) {
			if (entry.getValue() > max) {
				max = entry.getValue();
				maxDan = entry.getKey();
				joongbok = false;
			}
			else if(entry.getValue() == max) {
				joongbok = true;
			}
		}		

		if (joongbok) {
			System.out.println("?");
		} else {
			System.out.println(maxDan);
		}

	}
}
