package D3;

import java.util.Scanner;

public class 부분수열의합 {
	
	static int arr[];
	static int K;
	static int N;
	static int cnt;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
       
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			N=sc.nextInt();
			K=sc.nextInt();
			
			arr=new int[N];
			
			for (int j = 0; j < N; j++) {
				arr[j]=sc.nextInt();
			}
			cnt=0;
			recur(0,0);
			System.out.println(cnt);
		}
	}
	
	static void recur(int index, int sum) {
		if(sum==K) {
			cnt++;
			return;
		}
		if(index==N || sum>K) 
			return;
		recur(index+1,sum+arr[index]);
		recur(index+1,sum);
	}
}
