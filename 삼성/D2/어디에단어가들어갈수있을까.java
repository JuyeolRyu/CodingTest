package D2;

import java.util.Arrays;
import java.util.Scanner;

public class 어디에단어가들어갈수있을까 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int len=sc.nextInt();
			int num=sc.nextInt();
			int[][] arr=new int[len][len];
			for (int i = 0; i < len; i++) {
				for (int j = 0; j < len; j++) {
					arr[i][j]=sc.nextInt();
				}
			}
			for (int i = 0; i < arr.length; i++) {
				System.out.println(Arrays.toString(arr[i]));
			}
			System.out.print("#"+test_case+" ");
			
			int result=0;
			for (int i = 0; i < len; i++) {
				int cntH=0;
				int cntV=0;
				for (int j = 0; j < len; j++) {
					if(arr[i][j]==0) {
						if(cntH==num)
							result++;
						cntH=0;
					}
					else
						cntH++;
					if(arr[j][i]==0) {
						if(cntV==num)
							result++;
						cntV=0;
					}
					else
						cntV++;
				}
				if(cntH==num)
					result++;
				if(cntV==num)
					result++;
			}
			System.out.println(result);
		}
	}
}
