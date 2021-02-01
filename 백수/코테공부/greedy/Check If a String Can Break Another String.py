################################################################################
#1433. Check If a String Can Break Another String                              #
#https://leetcode.com/problems/check-if-a-string-can-break-another-string/     #
################################################################################

#s1의 순열중 하나가 s2의 순열중 하나보다 모든 인덱스에서 알파벳값이 더 크거나 같아야 한다.
#또는 반대의 경우
class Solution:
    #모든 인덱스에서 알파벳 값이 더 큰지 판단한다.
    def canBreak(self, s1: str, s2: str) -> bool:
        for i in range(len(s1)):
            #하나라도 작으면 실패
            if s1[i] < s2[i]:
                return False
        return True
            
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        #순서를 비교하기 위해서 정렬
        s1 = sorted(s1)
        s2 = sorted(s2)
        ans = False

        #두가지 경우 모두 판단한다
        #s1의 모든 알파벳이 더 크거나 같은 경우
        if s1[0] >= s2[0]:
            ans = ans or self.canBreak(s1,s2)
        
        #s2의 모든 알파벳이 더 크거나 같은 경우
        if s2[0] >= s1[0]:
            ans = ans or self.canBreak(s2,s1)
            
        return ans