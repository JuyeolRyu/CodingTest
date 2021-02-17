package BaekJoon;

import java.util.Scanner;

public class 재귀함수가뭔가요 {
	static int n;
	static String[] recurText= {"\"재귀함수가 뭔가요?\"",
			"\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.",
			"마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.",
			"그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."};
	static String[] recurText2= {"\"재귀함수가 뭔가요?\"",
			"\"재귀함수는 자기 자신을 호출하는 함수라네\"","라고 답변하였지."};
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		System.out.println("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.");
		recur(0);
	}
	
	private static void recur(int i) {
		if(i==n) {
			for (int k = 0; k < recurText2.length; k++) {
				for(int j=0;j<i;j++) {
					System.out.print("____");
				}
				System.out.println(recurText2[k]);
			}
			return;
		}
		
		for (int k = 0; k < recurText.length; k++) {
			for(int j=0;j<i;j++) {
				System.out.print("____");
			}
			System.out.println(recurText[k]);
		}
		recur(i+1);
		for(int j=0;j<i;j++) {
			System.out.print("____");
		}
		System.out.println("라고 답변하였지.");
	}
}
