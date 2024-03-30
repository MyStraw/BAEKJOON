import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Main {
	public static void main(String args[]) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int count = 0;
		for (int i = 0; i < N; i++) {
			Set<Character> cc = new HashSet<>();
			String group = sc.next();
			for (int j = 0; j < group.length() - 1; j++) {
				cc.add(group.charAt(j));
				if (group.charAt(j + 1) != group.charAt(j) && !cc.contains(group.charAt(j + 1))) {
					cc.add(group.charAt(j + 1));
				} else if (group.charAt(j + 1) != group.charAt(j) && cc.contains(group.charAt(j + 1))) {
					count++;
					break;
				}
			}
		}
		System.out.println(N - count);
	}
}