################################################################################
#1221. Split a String in Balanced Strings                                      #
#https://leetcode.com/problems/split-a-string-in-balanced-strings/             #
################################################################################

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_count = 0
        l_count = 0
        ans = 0
        for c in s:
            #l 과 r의 수를 세면서 간다
            if(c == 'R'):
                r_count += 1
            else:
                l_count += 1
            
            #두개의 수가 같아지면 한쌍 완성이므로 ans += 1
            if(r_count == l_count):
                ans += 1
                r_count = 0
                l_count = 0
        #쌍이 안갖춰진 경우 1 더해준다.
        if(r_count != 0 or l_count !=0):
            ans += 1
            
        return ans