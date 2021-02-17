package D3;

import java.util.Scanner;

public class 안경이없어 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc= new Scanner(System.in);
		
		String noBlank="CEFGHIJKLMNSTUVWXYZ";
		String oneBlank="ADOPQR";
		String justB="B";
		
		int T=sc.nextInt();
		
		for (int tc = 1; tc <= T; tc++) {
			System.out.print("#"+tc+" ");
			boolean check= true;
			String left=sc.next();
			String right=sc.next();
			
			if(left.length() != right.length()){
				System.out.println("DIFF");
			}
			else {
				for (int i = 0; i < left.length(); i++) {
					
					if( (noBlank.contains(left.substring(i, i+1)) && noBlank.contains(right.substring(i, i+1)))
					||	(oneBlank.contains(left.substring(i, i+1)) && oneBlank.contains(right.substring(i, i+1))) ||
					(justB.contains(left.substring(i, i+1)) && justB.contains(right.substring(i, i+1)))
							) {
						int j=1;}
					else
						check=false;
				}
				if(check)
					System.out.println("SAME");
				else
					System.out.println("DIFF");
			}
		}
		
	}
	
}
