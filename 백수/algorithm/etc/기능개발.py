#https://programmers.co.kr/learn/courses/30/lessons/42586
#기능개발(스택/큐)
import math
def solution(progresses, speeds):
    ans = []
    t = 0
    for i in range(len(speeds)):
        if progresses[i]+speeds[i]*t >= 100:
            ans[-1] += 1
            continue
        remain = 100-progresses[i]
        t = math.ceil(remain/speeds[i])
        ans.append(1)
    return ans


# import java.lang.Math;
# import java.util.*;

# class Solution {
#     public Integer[] solution(int[] progresses, int[] speeds) {
#         ArrayList<Integer> ans= new ArrayList<Integer>();
#         ArrayList<Integer> answer= new ArrayList<Integer>();
        
        
#         for(int i=0;i<progresses.length;i++){
#             int curDay = (int)Math.ceil((double)(100-progresses[i])/speeds[i]);
#             answer.add(curDay);
#         }
#         int prev = answer.get(0);
#         int cnt = 1;
#         for(int i=1;i<answer.size();i++){
#             if(answer.get(i) > prev){
#                 ans.add(cnt);
#                 prev=answer.get(i);
#                 cnt=1;
#             }else{
#                 cnt++;
#             }
#         }
#         ans.add(cnt);
        
#         Integer tmp[] = ans.toArray(new Integer[0]);
#         return tmp;
#     }
# }