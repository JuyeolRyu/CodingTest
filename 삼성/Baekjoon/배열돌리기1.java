package BaekJoon;

import java.util.Arrays;
import java.util.Scanner;

public class 배열돌리기1 {
	static int N,M;
	static int arr[][];
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		int R=sc.nextInt();
		arr=new int[N][M];
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				arr[i][j]=sc.nextInt();
			}
		}
		int test=Math.min(N, M)/2;
		for (int k = 0; k < R; k++) {
			for (int i = 0; i < test; i++) {//줄 갯수만큼			
				
				int temp=arr[i][i];
				
				for(int j = i + 1; j<=M-1-i;j++){//윗줄 왼쪽으로 보내기
			        arr[i][j-1] = arr[i][j];
			    }
				for(int j = i + 1 ; j<=N-1-i;j++){//오른줄 위쪽으로 보내기
			        arr[j-1][M-1-i] = arr[j][M-1-i];
			    }
				for (int j = M-2-i; j >= i ; j--) {//밑줄 오른쪽으로 보내기
					arr[N-1-i][j+1]=arr[N-1-i][j];
				}
				for (int j = N-2-i; j >= i; j--) {//왼줄 밑으로 보내기
					arr[j+1][i]=arr[j][i];
				}
				arr[i+1][i]=temp;
			}
		}
		
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(arr[i][j]+" ");
			}System.out.println();
		}
	}
}
