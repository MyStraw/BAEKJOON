import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		String S = sc.next();

		Set<Character> smupc = new HashSet<>();
		StringBuilder sb = new StringBuilder();

		int count = 0;
		for (int i = 0; i < S.length(); i++) {
			if (smupc.contains(S.charAt(i))) {
				count++;
			} else {
				smupc.add(S.charAt(i));
				sb.append(S.charAt(i));
			}
		}
		sb.append(count + 4).insert(0, N+1906).reverse().insert(0, "smupc_");
		System.out.println(sb);
	}
}