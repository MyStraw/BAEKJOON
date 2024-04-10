import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		int[][] lecture = new int[N][2];

		StringTokenizer st;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			lecture[i][0] = Integer.parseInt(st.nextToken());
			lecture[i][1] = Integer.parseInt(st.nextToken());
		}		
		Arrays.sort(lecture, (a, b) -> a[0] - b[0]);		
		PriorityQueue<Integer> pq = new PriorityQueue<>();	
		pq.add(lecture[0][1]);

		for (int i = 1; i < N; i++) {			
			if (lecture[i][0] >= pq.peek()) {
				pq.poll();
			}			
			pq.add(lecture[i][1]);
		}		
		System.out.println(pq.size());
	}
}