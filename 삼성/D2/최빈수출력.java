package D2;

import java.util.Arrays;
import java.util.Scanner;

public class 최빈수출력 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		for(int test_case=1;test_case<=T;test_case++) {
			int a=sc.nextInt();
			int[] arr=new int[101];
			
			for (int i = 0; i < 1000; i++) {
				arr[sc.nextInt()]++;
			}
			int max=0;
			int index=0;
			for (int i = 100; i > 0; i--) {
				if(max<arr[i]) {
					index=i;
					max=arr[i];
				}
			}
			System.out.println(index);
		}
	}
}
