#338. Counting Bits
#https://leetcode.com/problems/counting-bits/

#sol1 그냥 풀기
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0 for _ in range(num+1)]

        for i in range(1,num+1):
            ans[i] = bin(i)[2:].count('1')
        return ans

#sol2 Dynamic Programming
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1,num+1):
            if i%2 == 1:
                dp.append(dp[i-1]+1)
            else:
                dp.append(dp[i//2])
                
                
        return dp

#sol3 Dynamic Programming && bit cal
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = [0]
        for i in range(1, num+1):
            #비트 하나씩 왼쪽으로 보내면 2로 나눈것과 같음
            ans.append(ans[i >> 1] + i % 2)
        return ans