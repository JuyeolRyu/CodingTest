package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class 일곱난쟁이v2 {
	static int N;
	static int[] input;
	static boolean[] isSelected;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = 9;
		input = new int[N];
		isSelected = new boolean[N];
		for(int i=0; i<N; ++i) {
			input[i] = sc.nextInt();
		}
		Arrays.sort(input);
		generateSubSet(0,0,0);
	}
	
	private static void generateSubSet(int index,int cnt,int sum) { // count: 현재까지 고려한 원소 수, pick 은 지금까지 뽑은수
		if(cnt==7) {//끝까지 도달했거나, 7명이 뽑혔고, 더한것도 100이면	
			if(sum==100) {
				for (int i = 0; i < input.length; i++) {
					if(isSelected[i])
						System.out.println(input[i]);
				}
				System.exit(0);
			}
			return;
		}
		if(index==N) return;
		
		isSelected[index] = true;
		generateSubSet(index+1,cnt+1,sum+input[index]);//뽑았다면 pick 증가
		isSelected[index] = false;
		generateSubSet(index+1,cnt,sum);//뽑지않았다면.
	}
}


