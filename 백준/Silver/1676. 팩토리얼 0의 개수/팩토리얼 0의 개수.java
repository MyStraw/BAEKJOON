import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		BigInteger fact = BigInteger.ONE;
		
		for (int i = 2; i <= N; i++) {
			fact = fact.multiply(BigInteger.valueOf(i));
		}

		String factoStr = fact.toString();

		int count = 0;		
		for (int i = factoStr.length() - 1; i >= 0; i--) {
			if (factoStr.charAt(i) == '0') {
				count++;
			} else {
				break;
			}
		}

		System.out.println(count);
	}

}
