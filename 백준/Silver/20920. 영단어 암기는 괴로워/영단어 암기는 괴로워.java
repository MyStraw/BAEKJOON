import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		Map<String, Integer> map = new HashMap<>();

		List<String> list = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			String word = br.readLine();
			map.put(word, map.getOrDefault(word, 0) + 1);
		}
		List<Map.Entry<String, Integer>> mapList = new ArrayList<>(map.entrySet());		

		Collections.sort(mapList, new Comparator<Map.Entry<String, Integer>>() {
			@Override
			public int compare(Map.Entry<String, Integer> o1, Map.Entry<String, Integer> o2) {
				if (o2.getValue() - o1.getValue() == 0) {
					if (o2.getKey().length() - o1.getKey().length() == 0) {
						return o1.getKey().compareTo(o2.getKey());
					}
					return o2.getKey().length() - o1.getKey().length();
				}
				return o2.getValue() - o1.getValue();

			}
		});

		for (int i = 0; i < mapList.size(); i++) {
			if (mapList.get(i).getKey().length() >= M) {
				bw.write(mapList.get(i).getKey());
				bw.newLine();

			}
		}
		bw.flush();
		bw.close();
		br.close();

	}
}