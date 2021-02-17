package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class N과M_7 {
	
	static int M,N;
	static int[] input,numbers;
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		
		Scanner sc= new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		input = new int[N];
		numbers = new int[N];
		
		for (int i = 0; i < N; i++) {
			input[i]= sc.nextInt();
		}
		Arrays.sort(input);
		permutation(0);
		System.out.println(sb.toString());
	}
	
	private static void permutation(int cnt) {
		if(cnt==M) {
			for (int i = 0; i < M; i++) {
				sb.append(numbers[i]).append(" ");
			}
			sb.append("\n");
			return;
		}
		
		for (int i = 0; i < N; i++) {
			numbers[cnt]= input[i];
			permutation(cnt+1);
		}
	}
	
}
