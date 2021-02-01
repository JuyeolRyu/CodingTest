package D2;

import java.util.Arrays;
import java.util.Scanner;

public class 숫자를정렬하자 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int N=sc.nextInt();
			int[] arr=new int[N];
			for (int i = 0; i < arr.length; i++) {
				arr[i]=sc.nextInt();
			}
			Arrays.sort(arr);
			System.out.print("#"+test_case+" ");
			for (int i = 0; i < arr.length; i++) {
				System.out.print(arr[i]+" ");
			}
			System.out.println();
		}
	}
}
