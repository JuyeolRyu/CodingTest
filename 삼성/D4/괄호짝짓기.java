package D4;

import java.util.Scanner;
import java.util.Stack;

public class 괄호짝짓기 {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		for (int tc = 1; tc <= 10; tc++) {
			
			System.out.print("#"+tc+" ");
			Stack<Character> stack = new Stack();
			
			int n=sc.nextInt();
			String str=sc.next();
			int result=1;
			
			for (int i = 0; i < n; i++) {
				char c=str.charAt(i);//첫글자부터
				
				if(c == ')' && stack.peek() == '(') {
					if(!stack.pop().equals('('))
						result=0;
				}
                else if(c == ']' && stack.peek() == '[')
                {
					if(!stack.pop().equals('['))
						result=0;
				}
                else if(c == '}' && stack.peek() == '{')
                {
					if(!stack.pop().equals('{'))
						result=0;
				}
                else if(c == '>' && stack.peek() == '<')
                {
					if(!stack.pop().equals('<'))
						result=0;
				}
                else 
                	stack.push(c);
				
			} 	
			if(!stack.isEmpty()) result=0;
			System.out.println(result);
		}
	}
}
