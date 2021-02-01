############################################################################
#767. Reorganize String                                                    #
#https://leetcode.com/problems/reorganize-string/                          #
############################################################################

class Solution:
    def reorganizeString(self, S: str) -> str:
        set_s = set(S)
        dic = dict()
        ans = ""
        #문자들의 개수를 센다
        for c in set_s:
            dic[c] = S.count(c)
        
        while True:
            #문자 개수로 정렬
            dic = dict(sorted(dic.items(),key = operator.itemgetter(1),reverse = True))
            #0의개수 세기위한 변수
            cnt = 0
            #반복문 반복 횟수 저장
            chk = 0
            for c in dic:
                #뺄수 있는 경우
                if dic[c] > 0:
                    dic[c] -= 1
                    ans += c
                    chk += 1
                #못빼는 경우
                if dic[c] == 0:
                    cnt += 1
                #2번 반복한 경우
                if chk == 2:
                    break
            #모두다 0인 경우
            if cnt == len(dic):
                break
        if ans[-1] == ans[-2]:
            return ""
        return ans