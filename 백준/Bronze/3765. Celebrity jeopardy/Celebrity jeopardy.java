import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextLine()) {
			String sick = sc.nextLine().trim();
			System.out.println(sick);
		}
	}
}
