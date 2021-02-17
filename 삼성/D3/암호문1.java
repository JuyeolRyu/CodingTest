package D3;

import java.io.*;
import java.util.*;

public class 암호문1 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		
		for (int tc = 1; tc <= 10; tc++) {
			StringBuilder sb=new StringBuilder();
			sb.append("#"+tc+" ");
			
			int N=Integer.parseInt(br.readLine());
			
			LinkedList<String> link=new LinkedList<String>();
			StringTokenizer st=new StringTokenizer(br.readLine());
			
			for (int i = 0; i < N; i++) {
				link.add(st.nextToken());
			}
			
			int O=Integer.parseInt(br.readLine());
			StringTokenizer st2=new StringTokenizer(br.readLine());
			
			
			for (int i = 0; i < O; i++) {
				st2.nextToken();
				int x=Integer.parseInt(st2.nextToken());
				int y=Integer.parseInt(st2.nextToken());
				
				for (int j = 0; j < y; j++) {
					link.add(x+j,st2.nextToken());
				}
				
			}
			for (int i = 0; i < 10; i++) {
				sb.append(link.get(i)+" ");
			}
			System.out.println(sb.toString());
		}
		
	}

}
