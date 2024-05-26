import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);        
       
        int T = sc.nextInt();
        sc.nextLine();         
     
        for (int i = 0; i < T; i++) {           
            String input = sc.next();
            String output = sc.next();            
         
            if (input.equals(output)) {
                System.out.println("OK");
            } else {
                System.out.println("ERROR");
            }
        } 
    }
}