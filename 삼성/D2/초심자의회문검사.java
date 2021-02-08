package D2;

import java.util.Scanner;

public class 초심자의회문검사 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		for(int test_case=1;test_case<=T;test_case++) {
			String a=sc.next();
			char[] test= a.toCharArray();
			boolean t=true;
			
			for(int i=0;i<test.length/2;i++) {
				if(test[i]!=test[test.length-i-1]) {
					t=false;
					break;
				}
			}
			System.out.print("#"+test_case+" ");
			if(t)
				System.out.println("1");
			else
				System.out.println("0");
		}

		
	}
}
