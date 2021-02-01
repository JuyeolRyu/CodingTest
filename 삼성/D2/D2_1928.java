package D2;
import java.util.Scanner;

public class D2_1928 {

	public static void main(String args[]) throws Exception
	{
		String encoding = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
		
		Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();

		for(int test_case = 1; test_case <= T; test_case++)
		{
			String encodedString=sc.next();
			String temp="";
			for(int i = 0; i< encodedString.length();i+=4) {
				temp+=Integer.toBinaryString(encoding.indexOf(encodedString.charAt(i)));
				temp+=Integer.toBinaryString(encoding.indexOf(encodedString.charAt(i+1)));
				temp+=Integer.toBinaryString(encoding.indexOf(encodedString.charAt(i+2)));
				temp+=Integer.toBinaryString(encoding.indexOf(encodedString.charAt(i+3)));		
			}
			Character.toChars(Integer.parseInt(temp.substring(0, 8)));
			Character.toChars(Integer.parseInt(temp.substring(8, 16)));
			Character.toChars(Integer.parseInt(temp.substring(16, 24)));
			System.out.println();
			
		}
	}

}
