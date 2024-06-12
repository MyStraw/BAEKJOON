import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[][] map = new int[n][m];
		int[][] distance = new int[n][m];
		boolean[][] visited = new boolean[n][m];

		int startX = 0, startY = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
				distance[i][j] = -1;
				if (map[i][j] == 2) {
					startX = i;
					startY = j;
					map[i][j] = 1;
				}
			}
		}

		bfs(startX, startY, map, distance, visited);

	}

	public static void bfs(int startX, int startY, int[][] map, int[][] distance, boolean[][] visited) {
		int n = map.length;
		int m = map[0].length;
		Queue<int[]> que = new LinkedList<>();
		que.offer(new int[] { startX, startY });
		visited[startX][startY] = true;
		distance[startX][startY] = 0;

		while (!que.isEmpty()) {
			int[] current = que.poll();
			int x = current[0];
			int y = current[1];

			for (int i = 0; i < 4; i++) {
				int nx = x + dx[i];
				int ny = y + dy[i];

				if (nx >= 0 && ny >= 0 && nx < n && ny < m && map[nx][ny] == 1 && !visited[nx][ny]) {
					que.offer(new int[] { nx, ny });
					visited[nx][ny] = true;
					distance[nx][ny] = distance[x][y] + 1;
				}
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j] == 0) {
					System.out.print("0 ");
				}  else {
					System.out.print(distance[i][j] + " ");
				}
			}
			System.out.println();
		}
	}
}
