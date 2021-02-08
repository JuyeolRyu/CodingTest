package D2;

import java.util.Scanner;

public class 달팽이숫자 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			int length=sc.nextInt();
			int temp=length;
			
			int[][] array=new int[length][length];
			int cnt=1;
			int i=0; //x좌표
			int j=-1; //y좌표
			int change=1;
			while(true) {
				for(int k=0;k<temp;k++) {//가로
					j+=change;
					array[i][j]=cnt++;
				}
				if(cnt==length*length+1)
					break;
				temp--; // length 는 가로를 그릴떄마다 감소
				for(int k=0;k<temp;k++) {//세로
					i+=change;
					array[i][j]=cnt++;
				}
				change*=-1;
				
			}
			
			System.out.println("#"+test_case);
			
			for(i=0;i<length;i++) {
				for (j = 0; j < length; j++) {
					System.out.print(array[i][j]+" ");
				}
				System.out.println();
			}
		}
	}

}
