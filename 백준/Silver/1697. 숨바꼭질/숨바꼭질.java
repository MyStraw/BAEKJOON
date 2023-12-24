import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static final int MAX = 100000;

	public static int bfs(int start, int end) {
		boolean[] visited = new boolean[MAX + 1];
		Queue<int[]> queue = new LinkedList<>();
		queue.offer(new int[] { start, 0 });

		while (!queue.isEmpty()) {
			int[] current = queue.poll();
			int currentPosition = current[0];
			int currentTime = current[1];

			visited[currentPosition] = true;

			int[] nextPositions = { currentPosition - 1, currentPosition + 1, currentPosition * 2 };

			for (int nextPosition : nextPositions) {
				if (nextPosition >= 0 && nextPosition <= MAX && !visited[nextPosition]) {
					if (nextPosition == end) {
						return currentTime + 1; 
					}
					queue.offer(new int[] { nextPosition, currentTime + 1 }); // 다음 위치와 현재 시간 + 1을 큐에 넣음
				}
			}
		}
		return -1;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int K = Integer.parseInt(st.nextToken());

		if (N == K) {
			System.out.println(0);
		} else {
			System.out.println(bfs(N, K));
		}

	}

}
