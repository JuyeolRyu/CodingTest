package D3;

import java.util.Scanner;
public class 정삼각형분할놀이 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			
			long A=sc.nextLong();
			long B=sc.nextLong();
			long result=0;
			long sum=1;
			for (int i = 0; i < A/B; i++) {
				result+=sum;
				sum+=2;
			}
			System.out.println(result);
		}
	}
}
