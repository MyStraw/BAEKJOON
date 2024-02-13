import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int c1 = Integer.parseInt(st.nextToken());
		int c2 = Integer.parseInt(st.nextToken());
		int[] P = new int[n];
		int[] Q = new int[m];

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			P[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < m; i++) {
			Q[i] = Integer.parseInt(st.nextToken());
		}

		Arrays.sort(P);
		Arrays.sort(Q);

		int pIndex = 0;
		int qIndex = 0;
		int min = Integer.MAX_VALUE;
		int count = 0;

		while (pIndex < n && qIndex < m) {
            int distance = Math.abs(P[pIndex] - Q[qIndex]) + Math.abs(c1 - c2);
            if (distance < min) {
            	min = distance;
                count = 1;
            } else if (distance == min) {
                count++;
            }

            if (P[pIndex] < Q[qIndex]) {
                pIndex++;
            } else {
                qIndex++;
            }
        }

		bw.write(min + " " + count);
		bw.flush();
		bw.close();
	}

}
