package D3;

import java.util.Scanner;

public class 성공적인공연기획 {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		int T=sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			System.out.println("#"+tc+" ");
			
			String arr=sc.next();
			int[] user=new int[arr.length()];
			for (int i = 0; i < arr.length(); i++) {
				user[i]=arr.charAt(i)-48;
			}
			int result=0;
			int clap=user[0];
			for (int i = 1; i < user.length; i++) {
				if(i<=clap) {//기준조건보다 크면
					clap+=user[i];
					continue;
				}
				else {
					result+=i-clap;
					clap+=user[i]+(i-clap);
				}
			}
			System.out.println(result);
		}
	}
}
