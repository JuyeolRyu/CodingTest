package D5;

import java.io.*;
import java.util.*;

public class 최적경로 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); 
	static StringBuilder sb;
	
	static int company[]=new int[2];
	static int home[]=new int[2];
	static int customer[][];
	
	static int N,result;
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			sb = new StringBuilder();
			
			result=Integer.MAX_VALUE;
			N = Integer.parseInt(br.readLine());
			customer = new int[N][2];//
			sel=new boolean[N];
			StringTokenizer st = new StringTokenizer(br.readLine());
			
			company[0]= Integer.parseInt(st.nextToken());//회사
			company[1]= Integer.parseInt(st.nextToken());
			home[0]= Integer.parseInt(st.nextToken());//집
			home[1]= Integer.parseInt(st.nextToken());
			
			for (int i = 0; i < N; i++) {
				customer[i][0] = Integer.parseInt(st.nextToken()); //고객
				customer[i][1] = Integer.parseInt(st.nextToken());
			}
			permutation(company[0],company[1],0,0);//회사출발.
			
			sb.append("#" + tc + " "+result);
			
			System.out.println(sb.toString());
		}
	}
	
	static boolean sel[];
	
	public static void permutation(int x,int y,int range,int cnt) {//이전좌표기억
		if(cnt==N) {
			range=range+Math.abs(x-home[0])+Math.abs(y-home[1]);
			if(range<result)
				result=range;
			return;
		}
		else if(range >= result)
			return;
		
		for (int i = 0; i < N; i++) {
			if(sel[i])continue;
			sel[i]=true;
			permutation(customer[i][0], customer[i][1],range+Math.abs(x-customer[i][0])+Math.abs(y-customer[i][1]), cnt+1);
			sel[i]=false;
		}
	}
}
