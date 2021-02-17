package D3;

import java.util.Scanner;

public class 사랑의카운슬러v2 {
	
	static int N;
	static int[] x;
	static int[] y;
	static boolean[] sel;
	static long result;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			N=sc.nextInt();
			result=Long.MAX_VALUE;
			
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
	
	public static void permutation(int idx, int cnt) {
		if(cnt==N/2) {
			long X=0;
			long Y=0;
			for (int i = 0; i < N; i++) {
				if(sel[i]) {//더할 좌표계
					X+=x[i];
					Y+=y[i];
				}
				else{//뺄좌표계
					X-=x[i];
					Y-=y[i];
				}
			}
			if(result>X*X+Y*Y)
				result=X*X+Y*Y;
		}
		
		for (int i = idx; i < N; i++) {//뽑힌 종류가 중요하지 순서가 중요하진 않다.
			sel[i]=true;//다만 체크용으로 
			permutation(i+1,cnt+1);//나머지는 combination 코드와 유사하게
			sel[i]=false;
		}
	}
}