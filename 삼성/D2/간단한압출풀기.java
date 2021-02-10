package D2;

import java.util.Scanner;

public class 간단한압출풀기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int N=sc.nextInt();
			int cnt=0;
			System.out.println("#"+test_case);
			for (int i = 0; i < N; i++) {
				int c=sc.next().charAt(0);
				int num=sc.nextInt();
				
				for (int j = 0; j < num; j++) {
					System.out.printf("%c",c);
					cnt++;
					if(cnt==10) {
						System.out.println();
						cnt=0;
					}
				}
			}
			System.out.println();
		}
	}
}
