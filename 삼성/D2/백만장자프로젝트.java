package D2;

import java.util.Scanner;

public class 백만장자프로젝트 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			System.out.print("#"+test_case+" ");
			int N=sc.nextInt();
			long[] arr=new long[N];
			for (int i = 0; i < N; i++) {
				arr[i]=sc.nextInt();
			}
			long result=0;
			long max=arr[N-1];
			for (int i = N-1;i >=0; i--) {
				if(max > arr[i]) {
					result += max-arr[i];
				}
				else if (max <= arr[i]) {
					max=arr[i];
				}
			}
			System.out.println(result);
		}
	}

}
