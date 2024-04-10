import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int N = Integer.parseInt(br.readLine());
		Meeting[] meetings = new Meeting[N];

		StringTokenizer st;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			meetings[i] = new Meeting(start, end);
		}

		Arrays.sort(meetings); 
		int count = 0;
		int prevEndTime = 0;

		for (int i = 0; i < N; i++) {			
			if (meetings[i].start >= prevEndTime) {
				prevEndTime = meetings[i].end;
				count++;
			}
		}
		System.out.println(count);
	}
}

class Meeting implements Comparable<Meeting> {
	int start;
	int end;

	public Meeting(int start, int end) {
		this.start = start;
		this.end = end;
	}	
	@Override
	public int compareTo(Meeting o) {
		if (this.end == o.end) {
			return this.start - o.start;
		}
		return this.end - o.end;
	}
}