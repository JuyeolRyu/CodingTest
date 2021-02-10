package D3;

import java.util.Scanner;

public class 항구에들어오는배 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		
		int T=sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			int N=sc.nextInt();
			int arr[]=new int[N];
			boolean[] visit=new boolean[N];
			int result=0;
			for (int i = 0; i < N; i++) {
				arr[i]=sc.nextInt();
			}
			int gap=1;
		
			for (int i = 1; i < visit.length; i++) {
				if(!visit[i]) {//아직 안갔으면
					gap=arr[i]-arr[0];//새로운 gap
				}
				else//이미 갔던애면
					continue;

				int temp=arr[0]+gap;
				for (int j = 1; j < visit.length; j++) {
					if(temp==arr[j]) {//안갔고   ,  맞는 배의 주기가 존재하면 gap배수 올려주면서 체크
						if(temp==arr[0]+gap)//처음한번만 결과 up
							result++;
						visit[j]=true;
						temp+=gap;
					}
				}
			}
			System.out.println("#"+tc+" "+result);
		}
	}

}
