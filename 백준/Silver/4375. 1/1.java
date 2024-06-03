import java.math.BigInteger;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		while (sc.hasNextInt()) {
			int n = sc.nextInt();
			BigInteger num = BigInteger.ONE;
			int count = 1; 
			while (true) {
				if (num.mod(BigInteger.valueOf(n)).equals(BigInteger.ZERO)) {
					System.out.println(count);
					break;
				}
				num = num.multiply(BigInteger.TEN).add(BigInteger.ONE);
				count++;
			}
		}
	}
}
