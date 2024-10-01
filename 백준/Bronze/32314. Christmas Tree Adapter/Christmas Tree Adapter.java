import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
	
		int ampere = sc.nextInt();		
		int watt = sc.nextInt();
		int volt = sc.nextInt();
	
		int atapter = watt / volt;
	
		if (atapter >= ampere) {
			System.out.println(1);
		} else {
			System.out.println(0);
		}		

	}

}
