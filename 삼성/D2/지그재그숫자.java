package D2;

import java.util.Scanner;

public class 지그재그숫자 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int N=sc.nextInt();
			int odd=0;
			int even=0;
			int result=0;
			System.out.print( "#" + test_case +" " );
			for(int i = 1; i <= N ; i++ ) {
				if(i % 2 ==0)
					even+=i;
				else
					odd+=i;
				result= odd-even;
			}
			System.out.println(result);
		}
	}
}
