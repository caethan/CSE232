import java.io.*;
import java.util.*;

/**
 * Problem xxx: xxx
 */
public class Main {
	public static void main(String[] args) throws IOException {

		// For STDIN, put two stars below.
		// For File In, put one star below.
		/**/
		Scanner scanner = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
		/*/
		Scanner scanner = new Scanner(new BufferedReader(new InputStreamReader(new FileInputStream("sample.in"))));
		/**/

		while (scanner.hasNextInt()) {
			int n = scanner.nextInt();
			
			// Example: print the square of the number
			System.out.println(n*n);
		}
	}
}