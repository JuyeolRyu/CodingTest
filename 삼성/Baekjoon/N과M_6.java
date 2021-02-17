package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class N과M_6 {
	
	static int M,N;
	static int[] input,numbers;
	static boolean[] isSelected;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		input = new int[N];
		numbers = new int[N];
		isSelected= new boolean[N];
		
		for (int i = 0; i < N; i++) {
			input[i]= sc.nextInt();
		}
		Arrays.sort(input);
		combination(0,0);
		System.out.println(sb.toString());
	}
	
	private static void combination(int cnt,int start) {
		if(cnt==M) {
			for (int i = 0; i < M; i++) {
				sb.append(numbers[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = start; i < N; i++) {
			numbers[cnt]= input[i];
			combination(cnt+1,i+1);
		}
	}
	
}
