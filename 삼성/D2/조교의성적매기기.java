package D2;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 조교의성적매기기 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			System.out.println("#"+test_case);
			int N=sc.nextInt();
			int K=sc.nextInt();
			double[] result=new double[N];
			for (int i = 0; i < N; i++) {
				result[i]=sc.nextInt()*0.35+sc.nextInt()*0.45 + sc.nextInt()*0.2;
			}
			double target=result[K-1];
			Arrays.sort(result);
			int i;
			for (i = 0; i < N; i++) {
				if(target==result[i])
					break;
			}
			System.out.println(Arrays.toString(result));
			//int student=N-i-1;
			int ps=N/10;
			if(i/ps==9) System.out.println("A+");
			else if(i/ps==8) System.out.println("A0");
			else if(i/ps==7) System.out.println("A-");
			else if(i/ps==6) System.out.println("B+");
			else if(i/ps==5) System.out.println("B0");
			else if(i/ps==4) System.out.println("B-");
			else if(i/ps==3) System.out.println("C+");
			else if(i/ps==2) System.out.println("C0");
			else if(i/ps==1) System.out.println("C-");
			else if(i/ps==0) System.out.println("D0");
		}
	}
}
