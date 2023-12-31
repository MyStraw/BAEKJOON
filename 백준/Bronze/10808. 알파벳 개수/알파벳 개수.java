import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String s = scanner.nextLine();
        int[] alphabetCount = new int[26];
        
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            alphabetCount[currentChar - 'a']++;
        }
        
        for (int count : alphabetCount) {
            System.out.print(count + " ");
        }
        System.out.println();
    }

}
