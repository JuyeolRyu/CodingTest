package D2;

import java.util.Scanner;

public class 파리퇴치 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int N = sc.nextInt();
			int M= sc.nextInt();
			int[][] arr=new int[N][N];
			
			for (int i = 0; i < arr.length; i++) {
				for (int j = 0; j < arr.length; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			int result=0;
			for(int i=0;i<N-M+1;i++) {
				for (int j = 0; j < N-M+1; j++) {
					int sum=0;
					for (int p = 0; p < M; p++) {
						for (int q = 0; q < M; q++) {
							sum+=arr[i+p][j+q];
						}
					}
					if(result < sum)
						result=sum;
				}
			}
			System.out.println(result);
		}
	}

}
