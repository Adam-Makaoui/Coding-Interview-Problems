//import java.util.Scanner;

public class consectiveVowels {

		
	static char [] vowels = {'a', 'e', 'i', 'o', 'u'};
	
	static String test1true = "xaxexxiixxi";  // has 2 consective vowels
	static String test2false = "xexixa";  // has no consective vowels
	
	/**
	 *  determines if a character is in a character array
	 * @param c - character to test
	 * @param cArr - the given array
	 * @return true/false
	 */
	public static boolean containsChar (char c, char [] cArr) {
		
		for (char x: cArr) {
			if (x == c)
				return true;
		}
		// default case
		return false;
	} // ------------------------- End of Method ---------------------------------
	
	
	/** Tests if a given string contains consective vowels
	 * 
	 * @param str1 - String to test
	 * @return - true/false 
	 */
	public static boolean isConsec (String str1) {
	
	
	// char array of string
	char [] charStr = str1.toCharArray();
	
	for (int i = 0; i < charStr.length-1 ; i++) {
		
		char firstChar = charStr[i];  // first char in string
		char secondChar = charStr[i+1];
		
		// if vowels contains the first char of the string
		if (containsChar(firstChar, vowels)  && containsChar(secondChar, vowels) ) // if both vowels
			return true;
		
	}
	
	// default case
	return false;

	} // ------------------------- End of Method ---------------------------------
	
	// Unit testing 2 cases
	public static void main(String[] args) {
		
		// Unit testing - insert into function
		System.out.print("Expect output: true \nActual output: ");
		System.out.println(isConsec(test1true));
		
		System.out.print("\nExpect output: false \nActual output: ");
		System.out.println(isConsec(test2false));

		
	}
	
	

}
