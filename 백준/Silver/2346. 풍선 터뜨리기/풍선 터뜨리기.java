import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());

		int[] balloons = new int[n];
		boolean[] pop = new boolean[n];

		for (int i = 0; i < n; i++) {
			balloons[i] = Integer.parseInt(st.nextToken());
		}

		int currentIndex = 0;
		int move;
		int count = n;
		
		while (count > 0) {			
			System.out.print((currentIndex + 1) + " ");
			pop[currentIndex] = true;
			count--;

			if (count == 0)
				break;

			move = balloons[currentIndex];			
			while (move != 0) {
				currentIndex = (currentIndex + (move > 0 ? 1 : -1) + n) % n; 
				if (!pop[currentIndex]) { 
					move = move > 0 ? move - 1 : move + 1;
				}
			}
		}
	}
}