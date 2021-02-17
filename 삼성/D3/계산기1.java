package D3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class 계산기1 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		for (int tc = 1; tc <= 10; tc++) {
			int L=Integer.parseInt(br.readLine());
			
			char[] forward=br.readLine().toCharArray();
			char[] backward=new char[L];
			Stack<Character> stack=new Stack<Character>();
			int j=0;
			for (int i = 0; i < L; i++) {
				if(forward[i]!='+' && forward[i]!='*') {
					backward[j++]=forward[i];
				}
				else if(forward[i] == '+') {
                    while( stack.size() != 0) {//더하기는 바로
                    	backward[j++] = stack.pop();
                    }
                    stack.add(forward[i]);
                }
			}
			while(!stack.isEmpty()) {
				backward[j++]=stack.pop();
			}
			Stack<Integer> stack2=new Stack<Integer>();
			for (int i = 0; i < L; i++) {
				if(backward[i] != '+' && backward[i] != '*') {
					stack2.add(backward[i]-'0');
				}
				else {
					int num=stack2.pop();
					int num2=stack2.pop();
					int result;
					if(backward[i]=='+')
						result=num+num2;
					else
						result=num*num2;
					stack2.add(result);
				}
			}
			System.out.println("#"+tc+" "+ stack2.pop());
		}
	}
}
