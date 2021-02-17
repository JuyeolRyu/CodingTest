package D3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class 한빈이와SpotMart {
	
	static BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
	
	
	static int N;
	static int M;
	static boolean sel[];
	static int arr[];
	static int result;
	
	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		int T=Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			StringTokenizer st=new StringTokenizer(br.readLine());
			result=-1;
			N=Integer.parseInt(st.nextToken());
			M=Integer.parseInt(st.nextToken());
			arr= new int[N];
			
			st=new StringTokenizer(br.readLine());
			
			for (int i = 0; i < N; i++) {
				arr[i]=Integer.parseInt(st.nextToken());
			}
			
			snackComb(0,0,0);
			System.out.println("#"+tc+" "+result);
		}
	}
	static void snackComb(int idx,int cnt,int sum){
        if(cnt==2) {
        	if(sum <= M && result < sum)
        		result=sum;
        	return;
        }
        for (int i = idx; i < N; i++) {
        	snackComb(i+1,cnt+1,sum+arr[i]);
		}
    }
}
