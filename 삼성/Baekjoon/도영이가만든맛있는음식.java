package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class 도영이가만든맛있는음식 {
	
	static int N;
	static int arr[][];
	static int ans;
	static int temp;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		N = sc.nextInt();
		arr=new int[N][2];
		ans=Integer.MAX_VALUE;
		for (int i = 0; i < N; i++) {
			arr[i][0]=sc.nextInt();
			arr[i][1]=sc.nextInt();
		}
		temp=N;
		while(temp!=0) {
			combination(0,0,1,0);
			temp--;
		}
		
		System.out.println(ans);
	}
	
	public static void combination(int cnt, int start,int mul,int sum) {
		if(cnt==temp) {	
			int result= mul > sum ? mul-sum : sum-mul;
			if(result < ans)
				ans=result;
			return;
		}
		
		for (int i = start; i < N; i++) {//조합.
			combination(cnt+1,i+1,mul*arr[i][0],sum+arr[i][1]);
		}
	}

}
