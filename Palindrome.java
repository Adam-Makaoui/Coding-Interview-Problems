
public class Palindrome {

	
	static boolean checkPalindrome(String inputString) {
		
		boolean truth = false;

		// String to an array
		char charArr [] = inputString.toCharArray();

		// length of arr
		int tail = charArr.length-1;

		for ( char x: charArr ) {
		    if ( x == charArr[tail] )
		        truth = true;
		        
		    else {
		        truth = false;
		        return false; // time to exit
		        }
		    
		    // move the "tail" backwards
		    tail -= 1;

		}
		return truth;

		}
	
	public static void main(String[] args) {
		
		// unit testing
		
		String trueTest1 = "maam";
		String falseTest1 = "abaa";
		
		System.out.print("Expect output: true \nActual output: ");
		System.out.println(checkPalindrome(trueTest1));
		
		System.out.print("\nExpect output: false \nActual output: ");
		System.out.println(checkPalindrome(falseTest1));
		
		
	}
	

}
