import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int N = sc.nextInt();
		int M = sc.nextInt();
		int[] box = new int[N];

		int temp;

		for (int i = 0; i < N; i++) {
			box[i] = i + 1;

		} // 여기까지 N개의 박스에 1~N번까지 순서대로 공 넣기

		if (1 <= N && N <= 100 && 1 <= M && M <= 100) {
			for (int n = 0; n < M; n++) {
				int i = sc.nextInt();
				int j = sc.nextInt();
				if (1 <= i && i <= j && j <= N) {
					temp = box[i - 1];
					box[i - 1] = box[j - 1];
					box[j - 1] = temp;
				}
			}

		}
		for (int i = 0; i < N; i++) {
			System.out.print(box[i] + " ");
		}

	}
}
