#191. Number of 1 Bits
#https://leetcode.com/problems/number-of-1-bits/

#sol1
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
#sol2
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in bin(n):
            if i == '1':
                ans += 1
        
        return ans