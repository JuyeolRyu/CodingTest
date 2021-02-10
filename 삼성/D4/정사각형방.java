package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 정사각형방 {
	static BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder output = new StringBuilder();
	
	static int[] dx= {0,0,-1,1};
	static int[] dy= {-1,1,0,0};
	static int[][] arr;
	static int N;
	static int res[]=new int[2];
	
	//가봐야한다.
	//어떻게 짜야한다.
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		Scanner sc= new Scanner(System.in);
		int T = Integer.parseInt(input.readLine());
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			N= Integer.parseInt(input.readLine());
			
			arr= new int[N][N];
			res[0]=N*N+1;//방에 들어간 숫자
			res[1]=1;//이동횟수
			for (int i = 0; i < N; i++) {
				StringTokenizer str = new StringTokenizer(input.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(str.nextToken());
				}
			}
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					recur(i,j,1,arr[i][j]);//나 자신 포함하니까 1로 시작.
				}
			}
			System.out.println(res[0]+" "+res[1]);
		}
	}
	
	public static void recur(int y,int x,int cnt,int origin) {//현재 방위치. 이동횟수, 시작된 지점.
		for (int i = 0; i < dx.length; i++) {//사방으로.
			int cY=y+dy[i];
			int cX=x+dx[i];
			if(cY>=0 && cY<N && cX>=0 && cX<N && arr[y][x]+1==arr[cY][cX]) {//범위안넘어가면서 나보다 1이 크면.
				recur(cY,cX,cnt+1,origin); //이동하고 cnt+1
			}
		}
		//더 이동안하고 빠져나온다면.
		if( res[1] < cnt || (res[1] == cnt && res[0]>origin)) {//더 많이 이동한 친구가 있다면, 또는 똑같이 움직였는데, 새로온 애가 숫자가 더 적으면 
			res[0]=origin;
			res[1]=cnt;//정답을 등록해
		}
	}
}
