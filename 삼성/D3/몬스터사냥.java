package D3;

import java.util.Scanner;

public class 몬스터사냥 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			double damage=0;
			double D=sc.nextInt();
			double L=sc.nextInt()/100.0;
			double N=sc.nextInt();
			for (int i = 0; i < N; i++) {
				damage+= (D*(1+i*L));
			}
			System.out.println("#"+tc+" "+(int)damage);
		}
	}

}
