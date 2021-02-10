package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Ladder1 {//마지막열에서 사다리 살을 기억해둔다면?
	static int[] dx= {-1,0,1};//좌상우
	static int[] dy= {0,-1,0};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		//Scanner sc=new Scanner(System.in);
		for (int tc = 1; tc <=10; tc++) {
			//int T=sc.nextInt();
			int T=Integer.valueOf(br.readLine());
			System.out.print("#"+T+" ");
			
			StringTokenizer st;
			
			int[][] arr=new int[100][100];
			for (int i = 0; i < 100; i++) {
				st = new StringTokenizer(br.readLine(), " ");
				for (int j = 0; j < 100; j++) {
					arr[i][j]=Integer.valueOf(st.nextToken());
					
				}
			}
			int point;
			for(point=0;point<100;point++) {
				if(arr[99][point]==2) break; //끝점 찾기.
			}
			int y=99;
			int x=point;
			while(y>0) {
				if(x+dx[0] >= 0 && arr[y+dy[0]][x+dx[0]] == 1 ) {//좌가 1이면
					while( x-1 >= 0 && arr[y+dy[0]][x+dx[0]] != 0 )//좌가 0나올때까지 범위안에서
						x--;
				}
				else if( x+dx[2] <= 99 && arr[y+dy[2]][x+dx[2]] == 1) {//우가 1이면
					while( x+dx[2] <= 99 && arr[y+dy[2]][x+dx[2]] != 0 ) {//우가 0나올때 까지 범위안에서
						x++;
					}
				}
				y--;
			}
			System.out.println(x);
		}
	}
}
