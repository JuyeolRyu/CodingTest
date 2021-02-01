################################################################################
#921. Minimum Add to Make Parentheses Valid                                    #
#https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/          #
################################################################################
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        ans = 0
        f_p = 0

        for i in S:
            if(i == '('):   #여는 괄호의 개수 세주기
                f_p += 1
            else:           #닫는 괄호의 경우
                if(f_p > 0):#여는 괄호가 하나라도 앞에 나왔으면 여는괄호 하나 빼줌
                    f_p -= 1
                else:       #여는 괄호 맞는 쌍이 없으므로 ans += 1
                    ans += 1
                

        return ans + f_p    #ans 와 짝이 안맞는 여는 괄호 더해서 반환해줌