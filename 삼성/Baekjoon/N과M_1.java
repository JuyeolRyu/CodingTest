package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class N과M_1 {
	
	static int N,M;
	static boolean[] isSelected;
	static int arr[];
	static int res[];
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		
		res=new int[N];

		isSelected=new boolean[N+1];
		
		permutation(0);
	}
	
	static void permutation(int cnt) {
		if(cnt==M) {//기저조건
			for (int i = 0; i < M; i++) {
				System.out.print(res[i]+" ");
			}
			System.out.println();//결과
			return;
		}
		
		for (int i = 1; i <= N; i++) {// i: 시도하는 숫자.
			if(isSelected[i]) continue; //사용중이면 다음으로 가라.중복 허락하지 x
			
			res[cnt]=i;//뽑은거 넣는다.
			isSelected[i] = true;//뽑았다.
			
			permutation(cnt+1);			
			//i를 선택하고 나올 수 있는 모든 상태가 생성됨.
			
			isSelected[i] = false;
		}
	}
}
