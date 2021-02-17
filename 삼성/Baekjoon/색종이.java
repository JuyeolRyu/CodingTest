package BaekJoon;

import java.util.Scanner;

public class 색종이 {
	static int N;
	static int row,height,cnt;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[][] arr=new int[101][101];
		
		N=sc.nextInt();
		int cnt=0;
		for (int tc = 0; tc < N; tc++) {
			
			row = sc.nextInt();
			height = sc.nextInt();
			
			for (int i = height; i < height+10; i++) {
				
				for (int j = row; j < row+10; j++) {
					arr[i][j]=1;
				}
				
			}
			
			
		}
		for (int i = 0; i < 101; i++) {
			
			for (int j = 0; j < 101; j++) {
				if(arr[i][j]==1)
					cnt++;
			}
			
		}
		System.out.println(cnt);
	}
}
