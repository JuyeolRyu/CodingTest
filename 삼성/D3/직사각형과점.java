package D3;

import java.util.Scanner;

public class 직사각형과점 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		
		
		int T=sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			
			int in=0;
			int on=0;
			int out=0;
			
			int x1=sc.nextInt();
			int y1=sc.nextInt();
			int x2=sc.nextInt();
			int y2=sc.nextInt();
			
			
			int N=sc.nextInt();
			int[] x=new int[N];
			int[] y=new int[N];
			
			// 선위 (x1==a || x2==a) &&( y1<b<y2)
			// 직사각형 내부 (x1 < a < x2) && y1<b <y2
			for (int i = 0; i < N; i++) {
				if( ((x[i]==x1 || x[i]==x2) && ( y[i]>=y1 && y[i]<=y2))  ||  ((y[i]==y1 || y[i]==y2) && (x[i]>=x1 && x[i]<=x2)) ) {//세로선 위 
					on++;
				}
				else if(( x[i]>x1 && x[i]<x2) &&( y[i]>y1 && y[i]<y2) ) {
					in++;
				}
				else
					out++;
			}
			System.out.println("#"+tc+" "+in +" "+on+" "+out);
		}
	}
}
