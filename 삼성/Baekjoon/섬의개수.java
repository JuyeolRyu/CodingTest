package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class 섬의개수 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	static int W,H;
	
	static int[] dy= {-1,1,0,0,-1,-1,1,1}; //상하좌우 좌상 우상 좌하 우하
	static int[] dx= {0,0,-1,1,-1,1,-1,1};
	static int map[][];
			
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			W=Integer.parseInt(st.nextToken());
			H=Integer.parseInt(st.nextToken());
			if(W==0 && H==0)
				break;
			
			map=new int[H+2][W+2];
			
			for (int i = 1; i <= H; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 1; j <= W; j++) {
					map[i][j]=Integer.parseInt(st.nextToken());
				}
			}
			
			int cnt=0;
			for (int i = 1; i <= H; i++) {
				for (int j = 1; j <= W; j++) {
					if(map[i][j]==1) {
						cnt++;
						go(i,j);
					}
				}
			}
			
//			for (int i = 0; i < H+2; i++) {
//				System.out.println(Arrays.toString(map[i]));
//			}
			
			System.out.println(cnt);
		}

		
		
	}
	
	public static void go(int y,int x) {
		map[y][x]=0;
		for (int i = 0; i < 8; i++) {
			int tempY=y+dy[i];
			int tempX=x+dx[i];
			if(map[tempY][tempX]==1)
				go(tempY,tempX);
		}
	}
	
	
}
