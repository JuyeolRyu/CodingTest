package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 배열돌리기1지수팍{
	static int N, M, R;
	static int ary[][];

	static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		N = Integer.parseInt(st.nextToken());//세로길이
		M = Integer.parseInt(st.nextToken());//가로길이
		R = Integer.parseInt(st.nextToken());// 몇 번 돌려

		ary = new int[N][M];
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < M; j++)
				ary[i][j] = Integer.parseInt(st.nextToken());//변수받은거.
		}
	}

	static void solve() {
		
		for (int cycle = 0; cycle < R; cycle++) {//R번 돌릴게
			for (int idx = 0; idx < Math.min(N, M) / 2; idx++) {
				
				int temp = ary[idx][idx];//1 //6
				
				int i = idx, j = idx;
				// 가로 <
				for (; j < M - idx - 1; j++) //j=3
					ary[i][j] = ary[i][j + 1];
				// 세로 v
				for (; i < N - idx - 1; i++) //i=3
					ary[i][j] = ary[i + 1][j];
				// 가로 >
				for (; j > 0 + idx; j--)
					ary[i][j] = ary[i][j - 1];
				// 세로 ^
				for (; i > 1 + idx; i--)
					ary[i][j] = ary[i - 1][j];
				
				ary[i][j] = temp;
				
 			}
		}
	}

	static void view() {
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++)
				System.out.print(ary[i][j] + " ");
			System.out.println();
		}
		System.out.println();
	}

	public static void main(String[] args) throws IOException {
		init();
		solve();
		view();
	}
}
