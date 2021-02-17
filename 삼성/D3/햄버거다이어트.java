package D3;
import java.util.Scanner;

public class 햄버거다이어트 {
	static int ANSWER=0;
	static int cal[];
	static int score[];
	static boolean[] sel;
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		int test_case;
		test_case=sc.nextInt();
       
		for (int i = 0; i < test_case; i++) {
			ANSWER=0;
			int foodNum=sc.nextInt();
			int calCut=sc.nextInt();
			cal= new int[foodNum];
	        score = new int[foodNum];
	        sel= new boolean[foodNum];
	        
			for (int j = 0; j < foodNum ; j++){
	        	score[j]=sc.nextInt();
	            cal[j]=sc.nextInt();
	            sel[j]=false;
	        }
			int foodCases= 1 << foodNum;
			for(int q=0;q<foodCases;q++) {
				
	        	int sumCal=0;
	        	int sumScore=0;
	        	
				for(int p = 0; p<foodNum;p++) {
					
					if((q & (1 << p)) != 0) {
						
						sumCal+=cal[p];
						sumScore+=score[p];
					}
				}
	        	if(calCut >= sumCal && ANSWER <sumScore) 
	        		ANSWER=sumScore;
			}
			//hamRecur( 0, foodNum, calCut );
			System.out.printf("#%d %d\n",i+1,ANSWER);
			
		}
	}
}
//	//전부 다 가봄 (비 효율적)
//	static void hamRecur(int idx, int foodNum,int calCut){
//        if(idx==foodNum) {
//        	int sumCal=0;
//        	int sumScore=0;
//        	for(int i =0; i < foodNum; i++) {
//        		if(sel[i]) {
//        			sumCal+=cal[i];
//        			sumScore+=score[i];
//        		}
//        	}
//        	if(calCut >= sumCal && ANSWER <sumScore) 
//        		ANSWER=sumScore;
//        	return;
//        }
//        sel[idx]=true;
//        hamRecur(idx+1,foodNum,calCut);
//        sel[idx]=false;
//        hamRecur(idx+1,foodNum,calCut);
//    } 
//}