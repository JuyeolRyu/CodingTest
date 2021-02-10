package D3;

import java.util.Scanner;

public class 파도반수열 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
	    long arr[]=new long[100];
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			int n=sc.nextInt();
			
			arr[0]=1;arr[1]=1;arr[2]=1;
			for (int j = 3; j < 100; j++) {
				arr[j]=arr[j-2]+arr[j-3];
			}
			System.out.println(arr[n-1]);
		}
	}
}
