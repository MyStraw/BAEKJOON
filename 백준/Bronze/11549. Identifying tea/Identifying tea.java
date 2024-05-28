import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);        
        int T = sc.nextInt();      
        int[] answer = new int[5];
        for (int i = 0; i < 5; i++) {
            answer[i] = sc.nextInt();
        }      
        int count = 0;
        for (int i = 0; i < 5; i++) {
            if (answer[i] == T) {
                count++;
            }
        }    
        System.out.println(count);     
    }
}
