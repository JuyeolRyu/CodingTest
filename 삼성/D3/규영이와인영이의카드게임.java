package D3;

import java.util.Arrays;
import java.util.Scanner;

public class 규영이와인영이의카드게임 {
	
	static int win;
	static int lose;
	static int[] Q0;
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
       
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			win=0;
			lose=0;
			Q0=new int[9];
			int[] I0=new int[9];
			for (int j = 0; j < 9; j++) {
				Q0[j]=sc.nextInt();
			}
			int cnt=0;
			for (int j = 1; j <= 18; j++) {
				boolean temp=false;
				for (int j2 = 0; j2 < 9; j2++) {
					if(j==Q0[j2])
						temp=true;
				}
				if(temp==false)
					I0[cnt++]=j;
			}
			permutation(I0,0,9,9);
			System.out.println(win+" "+lose);
		}
	}
	
	static void permutation(int[] arr, int depth, int n, int r) {
		//순열 모르겠어서 개찐따 최광진은 검색해서품 
		//https://bcp0109.tistory.com/entry/%EC%88%9C%EC%97%B4-Permutation-Java
	    if (depth == r) {
	    	fight(arr);
	    	return;
	    }
	 
	    for (int i=depth; i<n; i++) {
	        swap(arr, depth, i);
	        permutation(arr, depth + 1, n, r);
	        swap(arr, depth, i);
	    }
	}
	
	static void fight(int[] arr) {
		int winCount=0;
		int loseCount=0;
		for (int i = 0; i < 9; i++) {
			if(Q0[i]<arr[i]) {
				loseCount+=Q0[i]+arr[i];
			}
			else if(Q0[i]>arr[i]) {
				winCount+=Q0[i]+arr[i];
			}
		}
		if(winCount>loseCount) win++;
		else if(winCount<loseCount) lose++;
	}
	
	public static void swap(int[] arr, int depth,int i) {
		int temp=arr[depth];
		arr[depth]=arr[i];
		arr[i]=temp;
	}
}
