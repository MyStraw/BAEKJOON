import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int cases = sc.nextInt();

		for (int i = 1; i <= cases; i++) {
			int max = 0; 
			for (int j = 0; j < 5; j++) {
				int weight = sc.nextInt(); 
				if (weight > max) {
					max = weight; 
				}
			}
			System.out.println("Case #" + i + ": " + max);
		}
		
	}

}
