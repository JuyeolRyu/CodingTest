package BaekJoon;

import java.util.*;
import java.util.Scanner;

public class 카드2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		
		Queue<Integer> que=new LinkedList<Integer>();
		int N =sc.nextInt();
		
		for (int i = 1; i <= N; i++) {
			que.add(i);
		}
		while(que.size()!=1) {
			que.poll();
			que.offer(que.poll());
		}
		System.out.println(que.poll());
	}
}


