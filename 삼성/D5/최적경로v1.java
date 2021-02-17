package D5;

import java.util.Scanner;

public class 최적경로v1 {
	
	static int N;
	static int[] customerX;
	static int[] customerY;
	static int companyX, companyY, homeX, homeY;
	
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for(int tc = 1; tc <= T; tc++) {
			
			N = sc.nextInt();
			customerX = new int[N];
			customerY = new int[N];
			companyX = sc.nextInt();
			companyY = sc.nextInt();
			homeX = sc.nextInt();
			homeY = sc.nextInt();
			
			for(int i = 0; i < N; i++) {
				customerX[i] = sc.nextInt();
				customerY[i] = sc.nextInt();
				
			}
			
			order = new int[N];// 내가 어떤 순서로뽑았는지 저장 배열
			check = new boolean[N];// 내가뽑았는지 아닌지 체크할 배열
			ans = 987654321; // 최솟값용
			perm(0);
			System.out.println("#" + tc + " " + ans);
		}
	}
	
	static int[] order;
	static boolean[] check;
	static int ans;
	
	static void perm(int idx) {
		if( idx == N ) {// N이 2라고 치면
			int dist = 0; //거리저장 변수
			int curX = companyX; //현재 x
			int curY = companyY; //현재 y
			for(int i = 0; i < N; i++) {
				dist += (Math.abs( curX - customerX[order[i]] ) + Math.abs( curY - customerY[order[i]]));
				curX = customerX[order[i]];
				curY = customerY[order[i]];
			}
			dist += (Math.abs( curX - homeX ) + Math.abs( curY - homeY ) ); 
			ans = Math.min(ans, dist);
			return;
		}
		
		for(int i = 0; i < N; i++) {
			if( !check[i] ) {
				order[idx] = i; // order[idx==0] = 1 , order[idx==1] = 0
				check[i] = true; // check[i==1] = true;
				perm(idx + 1); //
				check[i] = false;// 1을 안뽑은걸로할게. 0을안뽑은걸로 할게.
			}
		}
	}
}