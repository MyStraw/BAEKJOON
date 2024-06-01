import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);   
        double mpg = sc.nextDouble();        
        double LITERS_PER_GALLON = 3.785411784;
        double METERS_PER_MILE = 1609.344;
        double kmPerLiter = (mpg * METERS_PER_MILE) / (1000 * LITERS_PER_GALLON);
        double litersPer100km = 100 / kmPerLiter;
        System.out.printf("%.6f\n", litersPer100km);
    }
}
