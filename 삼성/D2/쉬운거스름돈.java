package D2;

import java.util.Arrays;
import java.util.Scanner;

public class 쉬운거스름돈 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			System.out.println("#"+test_case);
			int N=sc.nextInt();
			int[] arr= {50000,10000,5000,1000,500,100,50,10};
			int[] test=new int[8];
			
			for (int i = 0; i < test.length; i++) {
				test[i]=N/arr[i];
				N=N%arr[i];
			}
			for (int i = 0; i < test.length; i++) {
				System.out.print(test[i]+" ");
			}
		}
	}
}
