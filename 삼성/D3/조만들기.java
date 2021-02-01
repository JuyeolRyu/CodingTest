package D3;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 조만들기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			int N = sc.nextInt();
			int K = sc.nextInt();
			
			int gap=K*2-1;
			int result=0;
			for (int j = 1; j <= N; j++) {
				result+=(gap*(j/2))+(1*((j+1)/2));
			}
			for (int j = 0; j < K; j++) {
				if(N%2==1)System.out.print(result++ + " ");
				else System.out.print(result+" ");
			}System.out.println();
		}
	}
}
