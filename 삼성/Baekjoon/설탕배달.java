package BaekJoon;

import java.util.Scanner;

public class 설탕배달 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int N=sc.nextInt();
		int result= -1;
		for (int i = N/5; i >= 0; i--) {
			int j=N-i*5;
			if(j%3==0) {
				result=i+(j/3);
				break;
			}
		}
		System.out.println(result);
	}
}
