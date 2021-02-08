package D3;

import java.util.Scanner;
public class 화섭이의정수나열 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
	     
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			int N=sc.nextInt();
			String arr=new String();
			for (int j = 0; j < N; j++) {
				arr += sc.next();
			}
			int num=0;
			while(true) {
				String str=String.valueOf(num);
				if(arr.contains(str))
					num++;
				else
					break;
			}
			System.out.println(num);
		}
	}
}
