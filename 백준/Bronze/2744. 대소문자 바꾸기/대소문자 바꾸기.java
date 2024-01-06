import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String big = sc.next();
		
		StringBuilder sb = new StringBuilder();
		
		for (int i = 0; i< big.length(); i++) {
			char bs = big.charAt(i);
			if (Character.isUpperCase(bs)) {
				sb.append(Character.toLowerCase(bs));
			}
			else if(Character.isLowerCase(bs)) {
				sb.append(Character.toUpperCase(bs));
			}
		}
		
		System.out.println(sb);
		
	}
}
