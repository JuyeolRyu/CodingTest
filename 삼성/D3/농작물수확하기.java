package D3;

import java.util.Arrays;
import java.util.Scanner;

public class 농작물수확하기 {

	//static int[] dr= {-1,1,0,0}; //상하좌우
	//static int[] dc= {0,0,-1,1};
	//static int[] range= {0,0};
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
		
		for(int test_case = 1; test_case <= T ; test_case++ ) {
			System.out.println("#"+ test_case + " ");
			int N = sc.nextInt();
			int[][] arr=new int [N][N];
			int[][] result=new int[N][N];
			for (int i = 0; i < N; i++) {
				String str = sc.next();//next() 공백 기준 nextLine() 개행기준 nextline()은 다른거 다음에 쓰지 않기 enter를 챙겨감
				for (int j = 0; j < str.length(); j++) {
					arr[i][j]=str.charAt(j) - '0'; //j번째 문자. 문자를 뺴서 숫자로 집어넣음
				}
			}
			int[] range= {0,0};
			int mid=N/2; //중앙
			int temp=1;
			int sum=0;
			
			for (int i = 0; i < N; i++) {
				if(mid+range[0]==0)
					temp*=-1;
				for(int j=range[0];j<=range[1];j++) {
					sum+=arr[i][mid+j];
				}
				range[0]-=temp;
				range[1]+=temp;
			}
			System.out.println(sum);
		}
		
	}

}
/*  //1.델타합
for (int i = 0; i < N; i++) {
	for (int j = 0; j < N; j++) {
		int sum =arr[i][j]; //나를 더하고 시작
		for (int k = 0; k < 4; k++) {
			int nr = i + dr[k];
			int nc = j + dc[k];
			//농장밖으로 나가는 경우는 생략
			if( nr<0 || nr >=N || nc<0 || nc >=N)
				continue;
			sum+=arr[nr][nc];
		}
		result[i][j]=sum;
	}
}
*/