package D3;

import java.util.Scanner;

public class 알덴테스파게티 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			
			int N = sc.nextInt();
			int B = sc.nextInt();
			int E = sc.nextInt();
			int cnt=0;
			
			int arr[]= new int[N];
			
			for (int i = 0; i < N; i++) {
				arr[i] = sc.nextInt();
			}
			
			for (int i = 0; i < N; i++) {
				for (int j = B-E; j <= B+E; j++) {
					if(j%arr[i]==0) {
						cnt++;
						break;
					}
				}
			}
			System.out.println("#"+tc+" "+cnt);
		}
	}

}
