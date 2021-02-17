package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class 일곱난쟁이 {
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
		generateSubSet(0);//다 해봐야한다. 완전탐색
	}
	private static void generateSubSet(int count) { // count: 현재까지 고려한 원소 수
		if(count==N) {//끝까지 도달했으면.
			//true갯수가 7개이고 맞다면 더해서 100인지 체크
			int cnt=0;
			int sum=0;
			for (int i = 0; i < N; i++) {
				if(isSelected[i]) {
					cnt++;//true 7개인지 체크
					sum+=input[i];
				}
			}
			if(cnt==7 && sum==100) {//7명이면
				int[] dwarf=new int[7];
				int j=0;
				for (int i = 0; i < N; i++) {
					if (isSelected[i]) {
						dwarf[j++]=input[i];
					}
				}
				Arrays.sort(dwarf);
				for (int i = 0; i < dwarf.length; i++) {
					System.out.println(dwarf[i]);
				}
				System.exit(0);
			}
			return;
		}
		isSelected[count] = true;
		generateSubSet(count+1);
		isSelected[count] = false;
		generateSubSet(count+1);
	}
}
