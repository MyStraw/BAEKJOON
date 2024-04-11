import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		Nail doit[] = new Nail[n];

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int term = Integer.parseInt(st.nextToken());
			int limit = Integer.parseInt(st.nextToken());
			doit[i] = new Nail(term, limit);
		}

		Arrays.sort(doit);

		int last = 0;
		for (int i = n - 1; i >= 0; i--) {
			if (last <= doit[i].getLimit() && i != n - 1) {
				last = last - doit[i].getTerm();
			} else
				last = doit[i].getLimit() - doit[i].getTerm() + 1;
		}
		System.out.println(last - 1);

	}

	static class Nail implements Comparable<Nail> {
		private int term;
		private int limit;

		public Nail(int term, int limit) {
			this.term = term;
			this.limit = limit;
		}

		public int compareTo(Nail o) {
			return this.limit - o.limit;

		}

		public int getTerm() {
			return term;
		}

		public int getLimit() {
			return limit;
		}

	}

}
