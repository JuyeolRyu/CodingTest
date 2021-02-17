package BaekJoon;

import java.util.Scanner;

public class N과M_4 {
	
	static int N,M;
	static boolean[] isSelected;
	static int arr[];
	static int res[];
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		
		res=new int[N];

		isSelected=new boolean[N+1];
		
		combination(0,1);
		System.out.print(sb.toString());
	}
	
	static void combination(int cnt,int start) {
		if(cnt==M) {//기저조건
			for (int i = 0; i < M; i++) {
				sb.append(res[i]).append(" ");
			}
			sb.append("\n");//결과
			return;
		}
		
		for (int i = start; i <= N; i++) {// i: 시도하는 숫자.
			res[cnt]=i;//뽑은거 넣는다.
			combination(cnt+1,i);			
			//i를 선택하고 나올 수 있는 모든 상태가 생성됨.
		}
	}
}
