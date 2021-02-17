package D3;

import java.util.Scanner;

public class 삼성시의버스노선 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		
		int T=sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			int N=sc.nextInt();
			int bus[][]=new int[N][2];
			
			for (int i = 0; i < bus.length; i++) {
				bus[i][0]=sc.nextInt();
				bus[i][1]=sc.nextInt();
			}
			
			int P=sc.nextInt();
			
			for (int i = 0; i < P; i++) {
				int result=0;
				int C=sc.nextInt();
				for (int j = 0; j < bus.length; j++) {
					if(C >= bus[j][0] && C <= bus[j][1] ) {
						result++;
					}	
				}
				System.out.print(result+" ");
			}
			System.out.println();
		}
	}
}
