import java.util.HashSet;
import java.util.Set;

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {0,0};
        Set<Integer> set=new HashSet<Integer>();
        for(int i=0;i<lottos.length;i++){
            if(lottos[i]==0){
                answer[0]++;
            }
            set.add(lottos[i]);
        }
        for(int num:win_nums){
            if(set.contains(num)){
                answer[0]++;
                answer[1]++;
            }
        }
        int[] ans={Math.min(7-answer[0],6), Math.min(7-answer[1],6)};
        return ans;
    }
}