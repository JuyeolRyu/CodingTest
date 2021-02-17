package BaekJoon;

import java.util.Scanner;

public class 스위치켜고끄기 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int switchNum=sc.nextInt();
		int[] button=new int[switchNum];
		for (int i = 0; i < switchNum; i++) {
			button[i]=sc.nextInt();
		}
		int studentNum=sc.nextInt();
		int[][] student=new int[studentNum][2];
		for (int i = 0; i < studentNum; i++) {
			student[i][0]=sc.nextInt();
			student[i][1]=sc.nextInt();
		}
		for (int i = 0; i < studentNum; i++) {
			int range[]= {0,0};
			if(student[i][0]==1){//남자면
				for (int k = 1; k <= (switchNum/student[i][1]); k++) {
					int index=(student[i][1]*k)-1;
					button[index]=(button[index]+1)%2;
				}
			}
			else if(student[i][0]==2) {//여자면
				int temp=1;
				int mid=student[i][1]-1;
				//button[mid]=(button[mid]+1)%2;//나 자신은 미리바꿈
				while(true) {
					if(mid-temp < 0 || mid+temp >= switchNum || //바깥으로 나갔거나
							button[mid-temp]!=button[mid+temp]) {//좌우대칭이 아니면
						for (int k = mid-(temp-1); k <= mid+(temp-1); k++) {
							button[k]=(button[k]+1)%2;
						}
						break;
					}
					temp++;
			}
				
			}
		}
		for (int i = 1; i <= switchNum; i++) {
			System.out.print(button[i-1]+" ");
			if(i%20==0)
				System.out.println();
		}
		System.out.println();
	}

}
