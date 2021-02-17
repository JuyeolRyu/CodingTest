package D4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class 빠른휴대전화키패드 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static String numpad[]= {"",
			""   , "abc", "def",
			"ghi", "jkl", "mno",
			"pqrs","tuv","wxyz"};
	
	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int T = Integer.parseInt(br.readLine());
		
		for (int tc = 1; tc <= T; tc++) {
			st=new StringTokenizer(br.readLine());
			String S = st.nextToken();
			int sLen=S.length();
			int N=Integer.parseInt(st.nextToken());
			
			String arr[]=new String[N];
			
			st=new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i]=st.nextToken();
			}
			
			String arr2[]=new String[sLen];
			
			for (int i = 0; i < sLen; i++) {
				arr2[i]=numpad[Integer.parseInt(S.substring(i,i+1))];
			}
			int ans=0;
			
			for (int i = 0; i < N; i++) {//한 단어당
				boolean check = true;
				for (int j = 0; j < arr[i].length(); j++) {//한 글자당
					if(arr[i].length() != sLen) {//단어 길이 다르면 다음글자
						check=false; 
						break;
					}
					if(!arr2[j].contains(arr[i].substring(j,j+1))) {//단어 달라도 다음글자
						check=false;
						break;
					}
				}
				if(check)
					ans++;
			}
			
			System.out.println("#"+tc+" "+ans);
		}	
	}
}
