/**
 * Given a year, return the century it is in. The first century spans from the 
 * year 1 up to and including the year 100, the second - from the year 101 up 
 * to and including the year 200, etc.
 * 
 * @author Amak
 *
 */
public class centryFinder {

	static int test1 = 1905;
	static int test2 = 95;
	static int test3 = 2000;
	
	static int centuryFromYear(int year) {
		
	    // 1st centry
	    if (year <= 100)
	        return 1;
	        
	    // current centry e.g. 1900 = 19th centry
	     else if (year % 100 == 0)
	        return year/100;
	        
	    // next centry e.g. 1905 = 20th centry
	    else
	        return year/100 + 1;
	}
	
	// Unit testing
	public static void main(String[] args) {

		// Unit testing - insert into function
		System.out.print("Expect output: 20 \nActual output: ");
		System.out.println(centuryFromYear(test1));
		
		System.out.print("\nExpect output: 1 \nActual output: ");
		System.out.println(centuryFromYear(test2));
		
		System.out.print("\nExpect output: 20 \nActual output: ");
		System.out.println(centuryFromYear(test3));
	}

}
