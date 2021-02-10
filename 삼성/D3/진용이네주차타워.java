package D3;

import java.util.Arrays;
import java.util.Scanner;

public class 진용이네주차타워 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int T=sc.nextInt();
	     
		for (int i = 1; i <= T; i++) {
			System.out.print("#"+i+" ");
			int n=sc.nextInt();
			int m=sc.nextInt();
			
			int[] R_i=new int[n];//무게당 가격
			int[] W_i=new int[m];//무게

			int[] garage=new int[n];
			int[] wait=new int[2*m];
			for (int j = 0; j < n; j++) {
				R_i[j]=sc.nextInt();
			}
			for (int j = 0; j < m; j++) {
				W_i[j]=sc.nextInt();
			}
			
			for(int j = 0; j < 2*m; j++) {
				wait[j]=sc.nextInt();
			}
			
			int cnt=0;
			//n=2
			for(int j = 0; j < 2*m; j++) {
				if(wait[j]>0 && cnt<n)//공간이 있고 들어오는 차량이면,
					cnt++;
				else if(wait[j]>0 && cnt==n) {// 꽉찼는데 들어오는 차량이 있으면
					for (int j2 = j; j2 < 2*m; j2++) {
						if(wait[j2]<0) {
							int temp=wait[j2];//해당음수 저장.
							for (int k = j2; k > j; k--) {
								wait[k]=wait[k-1];
							}
							wait[j]=temp;
							break;
						}
					}
					j--;
				}
				else if(wait[j]<0){//공간이 있고 나가는 차량이면,
					cnt--;
				}
			}
			int result=0;
			for (int j = 0; j < 2*m; j++) {
				if(wait[j]>0) {
					for (int j2 = 0; j2 < n; j2++) {
						if(garage[j2]==0) {
							garage[j2]=wait[j];
							result+=R_i[j2]*W_i[wait[j]-1];
							wait[j]=0;
							break;
						}
					}
				}
				else if(wait[j]<0)
					for (int j2 = 0; j2 < n; j2++) {
						if(wait[j]*-1 == garage[j2]) {
							garage[j2]=0;
							wait[j]=0;
							break;
						}
					}
			}
			System.out.println(result);
		}
	}

}
