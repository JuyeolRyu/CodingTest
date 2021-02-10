package D3;

import java.util.Arrays;
import java.util.Scanner;

public class 진기의최고급붕어빵 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int tc = 1; tc <= T; tc++) {
        	System.out.println("#"+tc+" ");
            int N = sc.nextInt();
            int M = sc.nextInt();
            int K = sc.nextInt();
            
            int[] customer=new int[N];
            for (int i = 0; i < N; i++) {
				customer[i]=sc.nextInt();
			}
            Arrays.sort(customer);
            int test=0;
            boolean temp=true;
            for (int i = 0; i < N; i++) {
				test=customer[i]/M*K-i;
				if(test<=0) {
					temp=false;
					break;
				}
			}
            System.out.println("#"+tc+" "+ (temp?"Possible":"Impossible"));
            
//            Arrays.sort(customer);
//            int cnt=0;
//            int mul=0;
//            boolean temp=true;
//            for (int i = 0; i < (customer[N-1]/M+1); i++) {
//            	for (int j = 0; j < N; j++)
//                	if(customer[j] >= mul*M && customer[j] < (mul+1)*M)
//                		cnt++;
//                if(cnt>K*mul) {
//                	temp=false;
//                	break;
//                }
//                mul++;
//			}
//            if(temp)
//            	System.out.println("Possible");
//            else
//            	System.out.println("Impossible");
            	
            	
        }
	}
}
