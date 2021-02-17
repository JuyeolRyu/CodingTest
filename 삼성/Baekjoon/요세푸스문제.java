package BaekJoon;

import java.util.LinkedList;
import java.util.Scanner;

public class 요세푸스문제 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int N=sc.nextInt();
		int K=sc.nextInt();
		
		LinkedList<Integer> ll=new LinkedList<Integer>();
		StringBuilder sb=new StringBuilder();
		
		for (int i = 1; i <= N; i++) {
			ll.add(i);
		}
		
		int arr[]=new int[N];
		int j=0;
		int cnt=1;
		
		while(!ll.isEmpty()) {
			
			if(cnt%K==0) 
				arr[j++]=ll.remove();
			else
				ll.add(ll.remove());
			
			cnt++;
			
		}
		sb.append("<");
		
		for (int i = 0; i < arr.length; i++) {
			if(i==arr.length-1)
				sb.append(arr[i]+">");
			else
				sb.append(arr[i]+", ");
		}
		System.out.println(sb.toString());
	}
}
