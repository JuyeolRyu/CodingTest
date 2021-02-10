package D3;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class 암호생성기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		for (int tc = 1; tc <= 10; tc++) {
			sc.nextInt();//버려
			int[] arr= new int[8];
			Queue<Integer> que = new LinkedList<Integer>();
			for (int i = 0; i < arr.length; i++) {
				que.add(sc.nextInt());
			}
			int i=1;
			while(true) {
				int a=que.poll()-i++;
				if(a<=0) {
					que.add(0);
					break;
				}
				else que.add(a);
				
				if(i==6) {
					i=1;
				}
			}
			System.out.println("#"+tc+" ");
			for (int j = 0; j < arr.length; j++) {
				System.out.print(que.poll()+" ");
			}
		}
	}
}
