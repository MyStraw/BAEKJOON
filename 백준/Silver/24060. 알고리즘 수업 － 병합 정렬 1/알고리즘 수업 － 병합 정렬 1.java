import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int K; 
    static int count = 0;
    static int result = -1; 

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        int[] A = new int[N];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        merge_sort(A, 0, N - 1);

        System.out.println(result); 
    }
 
    static void merge_sort(int[] A, int p, int r) {
        if (p < r) {
            int q = (p + r) / 2; 
            merge_sort(A, p, q); 
            merge_sort(A, q + 1, r); 
            merge(A, p, q, r);
        }
    }

  
    static void merge(int[] A, int p, int q, int r) {
        int[] tmp = new int[r - p + 1];
        int i = p, j = q + 1, t = 0;
      
        while (i <= q && j <= r) {
            if (A[i] <= A[j]) {
                tmp[t] = A[i];
                count++; 
                if (count == K) {
                    result = A[i]; 
                }
                t++;
                i++;
            } else {
                tmp[t] = A[j];
                count++;
                if (count == K) {
                    result = A[j];
                }
                t++;
                j++;
            }
        }
      
        while (i <= q) {
            tmp[t] = A[i];
            count++;
            if (count == K) {
                result = A[i];
            }
            t++;
            i++;
        }

        while (j <= r) {
            tmp[t] = A[j];
            count++; 
            if (count == K) {
                result = A[j];
            }
            t++;
            j++;
        }
     
        for (int k = 0; k < tmp.length; k++) {
            A[p + k] = tmp[k];
        }
    }
}