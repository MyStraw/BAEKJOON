class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int [] student = new int [n+1];
        for (int i = 1; i<=n ; i++){
            student[i] = 1;
        }
        for (int l : lost){
            student[l]--;
        }
        
        for (int r : reserve){
            student[r]++;
        }
        
        for (int i = 1; i<=n;i++){
            if (student[i]>1){
                if (i>1 && student[i-1] == 0){
                    student[i]--;
                    student[i -1]++;
                
            }else if (i<n && student[i+1] == 0){
                student[i]--;
                student[i + 1]++;
                }
            }
        }                
        int answer = 0;
        for (int i = 1; i<=n;i++){
            if (student[i]>0){
                answer++;
            }
        }      
        
        return answer;
    }
}