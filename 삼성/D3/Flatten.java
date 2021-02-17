package D3;

import java.util.Arrays;
import java.util.Scanner;

public class Flatten {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		
		for (int tc = 1; tc <= 10; tc++) {
			System.out.println("#"+tc+" ");
			
			int dump=sc.nextInt();
			int arr[]=new int[100];
			
			for (int i = 0; i < 100; i++) {
				arr[i]=sc.nextInt();
			}
			
			Arrays.sort(arr);
			
			int result = arr[0] - arr[99];
			int cnt = 0;
			
			while(dump!=0) {
				if(arr[99]-arr[0]<=0) break;
				int j=0;
				for(j = 1; j < dump; j++) {
					if(arr[j]!= arr[0] || arr[99-j] != arr[99])
						break;
				}
				if(j>dump) {
					j=dump;
					dump-=j;
				}
				else
					dump-=j;
					
				for(int k = 0; k < j; k++) {
					arr[k]++;
					arr[99-k]--;
				}
				Arrays.sort(arr);
			}
			System.out.println(arr[99]-arr[0]);
		}
	}
}
