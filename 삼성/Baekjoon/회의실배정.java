package BaekJoon;

import java.util.*;

public class 회의실배정 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		
		int[][] arr=new int[N][2];
		
		for (int i = 0; i < N; i++) {
			arr[i][0]=sc.nextInt();
			arr[i][1]=sc.nextInt();
		}
		//첫시간이 가장 작은 것들중 시간이 제일 작은것을 고르고, 그리고 그다음 부터는 그 끝나는 시간에 맞춰서 찾기
		//가장 끝나는 시간이 빠른걸 찾기.
		
		Arrays.sort(arr, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				
				if(o1[1] == o2[1]) {
					return o1[0] - o2[0];
				}
				
				return o1[1] - o2[1];
			}
			
		});
		

		
		int cnt=0;
		int endTimeResearch=0;
		
		for (int i = 0; i < N; i++) {
			
			if(endTimeResearch <= arr[i][0]) {
				endTimeResearch = arr[i][1];
				cnt++;
			}
			
		}
		System.out.println(cnt);
	}
}
