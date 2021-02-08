package D3;

import java.util.Scanner;

public class 기차사이의파리 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			System.out.print("#"+ test_case + " ");
			
			double D,A,B,F;
			D=sc.nextInt();
			A=sc.nextInt();
			B=sc.nextInt();
			F=sc.nextInt();
			
			System.out.printf("%.10f\n",(D/(A+B))*F);
		}
	}

}
