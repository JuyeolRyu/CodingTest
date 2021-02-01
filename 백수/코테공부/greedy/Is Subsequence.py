############################################################################
#392. Is Subsequence                                                       #
#https://leetcode.com/problems/is-subsequence/                             #
############################################################################

#sol 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx = -1
        for cs in s:
            if cs not in t:
                return False
            else:
                check = True
                #t에서 탐색 ==> 이전 값의 인덱스보다 현재 문자의 인덱스가 더 크면 idx 갱신후 break
                for i in range(len(t)):
                    if cs == t[i] and i>idx:
                        idx = i
                        check = False
                        break
                
                #찾던게 뒤에 없는 경우
                if check:
                    return False
                
        return True

#sol 2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #다 비웠으면 s가 t의 substring이므로 true 반환
        if s == "":
            return True
        
        #s[0]이 t에 있다면 재귀로 다음 문자 탐색, 문자열도 갱신해준다
        if s[0] in t:
            return self.isSubsequence(s[1:], t[t.index(s[0])+1 : ])
        #s[0]이 t에 없는 경우 False 반환
        else:
            return False
                