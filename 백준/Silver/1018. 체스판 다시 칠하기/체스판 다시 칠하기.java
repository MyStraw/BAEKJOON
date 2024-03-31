import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		char[][] board = new char[N][M]; //입력받는 체스판

		for (int i = 0; i < N; i++) {
			board[i] = br.readLine().toCharArray();
		}

		int minCount = Integer.MAX_VALUE;
		for (int row = 0; row <= N - 8; row++) {
			for (int col = 0; col <= M - 8; col++) {
				minCount = Math.min(minCount, calculate(board, row, col));//if로 하는 min값 줄여서 이걸로.
			}
		}

		System.out.println(minCount);

	}

	public static int calculate(char[][] board, int row, int col) {
		int whiteStartCount = 0;
		int blackStartCount = 0;

		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				char expectWhiteFirst = ((i + j) % 2 == 0) ? 'W' : 'B';
				char expectBlackFirst = ((i + j) % 2 == 0) ? 'B' : 'W';

				char equalBoard = board[row + i][col + j];

				if (equalBoard != expectWhiteFirst) {
					whiteStartCount++;
				}
				if (equalBoard != expectBlackFirst) {
					blackStartCount++;
				}

			}

		}

		return Math.min(whiteStartCount, blackStartCount);

	}

}
