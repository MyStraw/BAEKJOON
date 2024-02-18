import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        int s1 = scanner.nextInt();
        int s2 = scanner.nextInt();
        
        if (s1 * 2 >= s2) {
            System.out.println("E");
        } else {
            System.out.println("H");
        }
    }
}
