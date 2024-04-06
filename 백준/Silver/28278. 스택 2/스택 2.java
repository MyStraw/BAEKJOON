import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	public static void main(String args[]) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine());

		IntStack stack = new IntStack(N);
		while (N-- > 0) {
			String[] order = br.readLine().split(" ");
			int X;

			switch (order[0]) {
			case "1":
				X = Integer.parseInt(order[1]);
				stack.push(X);
				break;

			case "2":
				bw.write(String.valueOf(stack.pop()) + "\n");
				break;

			case "3":
				bw.write(String.valueOf(stack.size()) + "\n");
				break;

			case "4":
				bw.write(String.valueOf(stack.empty()) + "\n");
				break;

			case "5":
				bw.write(String.valueOf(stack.peek()) + "\n");
				break;
			}
		}
		bw.flush();
		bw.close();
	}

	static class IntStack {
		int volume;
		int point;
		int stack[];

		IntStack(int N) {
			point = 0;
			volume = N;
			stack = new int[N];
		}

		int push(int X) {
			stack[point] = X;
			return stack[point++];
		}

		int pop() {
			if (point <= 0) {
				return -1;
			}
			return stack[--point];
		}

		int size() {
			return point;
		}

		int empty() {
			if (point <= 0) {
				return 1;
			}
			return 0;
		}

		int peek() {
			if (point > 0) {
				return stack[point - 1];
			}
			return -1;
		}
	}
}