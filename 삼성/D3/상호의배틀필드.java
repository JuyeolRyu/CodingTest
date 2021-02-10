package D3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 상호의배틀필드 {
	
	static StringTokenizer st;
	
	static int[] dx= {0,0,-1,1};//상하좌우 0 1 2 3
	static int[] dy= {-1,1,0,0};
	static char[] dc= {'^','v','<','>'};
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T=Integer.valueOf(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			st = new StringTokenizer(br.readLine());
			int H=Integer.valueOf(st.nextToken());// 문제에서 주어지는 값, 문제를 풀기위한 값.  앞으론 static하게
			int W=Integer.valueOf(st.nextToken());
			
			char field[][]=new char[H][W];
			
			for (int i = 0; i < H; i++) {
				char[] map=br.readLine().toCharArray();
				field[i]=map;
			}
			int N=Integer.valueOf(br.readLine());
			char input[]=br.readLine().toCharArray();
			int x = 0,y = 0;
			
			loop: for (y = 0; y < H; y++) {
				for (x = 0; x < W; x++) {
					if( field[y][x] == '^' || field[y][x] == 'v' || field[y][x] ==  '<' || field[y][x] == '>')
						break loop;
				}
			}
			int dir= (field[y][x]==dc[0] ? 0 : (field[y][x]==dc[1] ? 1 : (field[y][x]==dc[2]? 2 : 3 )));//방향을 초기화
			
			for (int cnt = 0; cnt < N; cnt++) {
				if(input[cnt]=='S') {//쐈으면
					int bX=x;
					int bY=y;
					while( bX >= 0 && bX < W && bY >= 0 && bY < H ) {
						if(field[bY][bX]=='*') {//돌벽만나면
							field[bY][bX]='.';//쾅
							break;
						}
						else if(field[bY][bX]=='#')//철벽만나면 끝
							break;
						bX+=dx[dir];
						bY+=dy[dir];
					}
					continue;
				}
				else{
					dir = (input[cnt]=='U' ? 0 : (input[cnt]=='D' ? 1 : (input[cnt]=='L' ? 2 : 3 ))); 
					if(y+dy[dir] >=0 && y+dy[dir] < H && x+dx[dir] >=0 && x+dx[dir] < W && field[y+dy[dir]][x+dx[dir]]=='.') {//밖으로 안나가고 평지면
						field[y][x]='.';
						y=y+dy[dir];
						x=x+dx[dir];
						field[y][x]=dc[dir]; //이동하고 고개돌림
					}
					else
						field[y][x]=dc[dir];//아니면 입력방향으로 고개만 돌림
				}	
			}
			for (int i = 0; i < H; i++) {
				for (int j = 0; j < W; j++) {
					System.out.print(field[i][j]);
				}
				System.out.println();
			}
		}
	}
}
		

