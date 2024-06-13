import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());

		long[] oasis = new long[N];

		for (int i = 0; i < N; i++) {
			oasis[i] = Integer.parseInt(br.readLine());
		}

		Stack<Now> stack = new Stack<>(); // 현재 잡고있는 {애 , 애의 카운트}
		long totalCount = 0; // 개별 카운트를 따로 세서 합쳐보자

		for (int i = 0; i < N; i++) {
			long nowAe = oasis[i];// 현재 내가 잡고있는 애
			long nowCount = 1;// 지금 잡고있는애 카운트.

			while (!stack.isEmpty() && stack.peek().nowPerson <= nowAe) {
				Now top = stack.pop();
				totalCount += top.nowCount;

				if (top.nowPerson == nowAe) { // 같은키 수 올리기
					nowCount += top.nowCount;
				}
			}
			if (!stack.isEmpty()) {
				totalCount++;
			}

			stack.push(new Now(nowAe, nowCount));
		}
		System.out.println(totalCount);

	}
}

class Now {
	long nowPerson;
	long nowCount;

	Now(long nowPerson, long nowCount) {
		this.nowPerson = nowPerson;
		this.nowCount = nowCount;
	}
}
