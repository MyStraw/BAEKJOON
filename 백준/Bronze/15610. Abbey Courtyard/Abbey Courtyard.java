import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));		
		long area = Long.parseLong(reader.readLine());	
		double sideLength = Math.sqrt(area);	
		double total = 4 * sideLength;	
		System.out.printf("%.9f\n", total);
	}

}
