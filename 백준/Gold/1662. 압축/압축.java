import java.util.Scanner;
import java.util.Stack;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String S = sc.next();
		System.out.println(alzip(S));
	}

	private static int alzip(String s) {
		Stack<Integer> stack = new Stack<>();
		int nowLen = 0;
		int i = 0;
		while (i < s.length()) {
			char ch = s.charAt(i);
			if (Character.isDigit(ch) && i + 1 < s.length() && s.charAt(i + 1) == '(') {				
				stack.push(nowLen);
				stack.push(ch - '0');
				nowLen = 0;
				i++;
			} else if (ch == ')') {
				int gophagi = stack.pop();
				int lastLen = stack.pop();
				nowLen = lastLen + gophagi * nowLen;
			} else if (ch != '(') {
				nowLen++;
			}
			i++;
		}
		return nowLen;
	}
}
