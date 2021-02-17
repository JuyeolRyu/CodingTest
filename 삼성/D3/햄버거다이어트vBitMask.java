package D3;

import java.util.Scanner;

public class 햄버거다이어트vBitMask {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			
			int answer=0;
			
			int N=sc.nextInt();
			int arr[][]= new int[N][2];
			
			int K = sc.nextInt();
			
			for (int i = 0; i < N; i++) {
				arr[i][0]=sc.nextInt();
				arr[i][1]=sc.nextInt();
			}
			
			int flag = 1 << N;
			
			for (int i = 0; i < flag; i++) {
				
				int sumCal = 0;
				int sumTaste = 0;
				
				for (int j = 0; j < N; j++) {
					
					if( (i & ( 1 << j )) != 0 ) {
						sumCal+=arr[j][1];
						sumTaste+=arr[j][0];
					}
				}
				
				if (sumCal <= K && answer < sumTaste) {
					answer = sumTaste;
				} 
			}
			
			System.out.println(answer);
		}
	}
}
