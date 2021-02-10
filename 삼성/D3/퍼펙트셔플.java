package D3;

import java.util.Scanner;

public class 퍼펙트셔플 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		int T=sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			int N=sc.nextInt();
			String str[]= new String[N];
			
			for (int i = 0; i < N; i++) {
				str[i]=sc.next();
			}
			int j=0;
			int odd=0;
			int even=(N+1)/2;
			while(j!=N) {			
				if(j%2==0) {
					System.out.print(str[odd++]+ " ");
				}
				else {
					System.out.print(str[even++]+" ");
				}			
				j++;
			}	
		}
	}
}
