package D3;

import java.util.Scanner;

public class 사랑의카운슬러 {//실패
	
	static int N;
	static int[] x;
	static int[] y;
	static boolean[] sel;
	static int[][] couple;
	static long result;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			N=sc.nextInt();
			result=Long.MAX_VALUE;
			couple=new int[N/2][2];
			
			x=new int[N];
			y=new int[N];
			sel=new boolean[N];
			
			for (int i = 0; i < N; i++) {
				x[i]=sc.nextInt();
				y[i]=sc.nextInt();
			}
			
			permutation(0,0);
			
			System.out.println("#"+tc+" "+ result);
		}
	}
	
	public static void permutation(int idx, int cnt) {//
		if(idx==N/2) {
			for (int i = 0; i < N/2; i++) {
				System.out.print(i+"번째 벡터"+couple[i][0]+" , "+couple[i][1] +"  ");
			}
			
			long sumX=0;
			long sumY=0;
			
			for (int i = 0; i < couple.length; i++) {
				sumX+=couple[i][0];
				sumY+=couple[i][1];
			}
			
			if(result>sumX*sumX+sumY*sumY)
				result=sumX*sumX+sumY*sumY;
			
			return;
		}
		
		if(cnt==2) {//1커플 완성
			
			permutation(idx+1,0);
			
			return;
		}
		for (int i = 0; i < N; i++) {
			if(sel[i]) continue;
			sel[i]=true; //뽑았어
			if(cnt%2==0) {//처음거는 집어넣고
				couple[idx][0]=x[i];
				couple[idx][1]=y[i];
			}
			else {
				couple[idx][0]-=x[i]; //두번째꺼는 빼서 벡터로 변환
				couple[idx][1]-=y[i];
			}
			permutation(idx,cnt+1);
			sel[i]=false;//안 뽑았어
		}
	}
}
