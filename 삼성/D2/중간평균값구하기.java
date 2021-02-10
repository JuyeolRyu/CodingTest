package D2;

import java.util.Arrays;
import java.util.Scanner;

public class 중간평균값구하기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int[] arr= new int[10];
			System.out.print("#"+test_case+" ");
			for (int i = 0; i < arr.length; i++) {
				arr[i]=sc.nextInt();
			}
			Arrays.sort(arr);
			System.out.println(Arrays.toString(arr));
			int sum=0;
			for(int i=1;i<arr.length-1;i++) {
				sum+=arr[i];
			}
			System.out.println(Math.round(sum/8.0));
		}
	}
}
