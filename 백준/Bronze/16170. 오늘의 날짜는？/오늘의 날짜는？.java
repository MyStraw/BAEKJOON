import java.time.LocalDate;
import java.time.ZoneId;

public class Main {
	public static void main(String[] args) {
		
		
		LocalDate seoulnow = LocalDate.now(ZoneId.of("Asia/Seoul"));		
		
		int year = seoulnow.getYear();
		int month = seoulnow.getMonthValue();
		int day = seoulnow.getDayOfMonth();
		
		System.out.println(year);
		System.out.println(month);
		System.out.println(day);
	}

}
