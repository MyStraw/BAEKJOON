class Solution {
    public int solution(int[][] sizes) {       
        for (int i = 0; i < sizes.length; i++) {
			if (sizes[i][0] < sizes[i][1]) {
				int temp = sizes[i][1];
				sizes[i][1] = sizes[i][0];
				sizes[i][0] = temp;
			}
		}

		int apMax = 0;
		int duiMax = 0;
		for (int i = 0; i < sizes.length; i++) {
			if (sizes[i][0] > apMax) {
				apMax = sizes[i][0];
			}
			if (sizes[i][1] > duiMax) {
				duiMax = sizes[i][1];
			}
		}
        int answer = apMax * duiMax;
        return answer;
    }
}