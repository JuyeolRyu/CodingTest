############################################################################################
#1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K                         #
#https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/#
############################################################################################
class Solution:
    #피보나치
    def fibonacci(self,k,prev_n):
        #k보다 큰 값이 오면 바로 전 값 반환
        if prev_n[0] + prev_n[1] > k:
            return prev_n[1]
        #그 외의 경우 다음 수로 탐색 시작
        rst = self.fibonacci(k,[prev_n[1], prev_n[0] + prev_n[1]])
        return rst
    def findMinFibonacciNumbers(self, k: int) -> int:
        #피보나치 초반인 경우 바로 값 반환
        if k == 1 or k == 2:
            return 1
        ans = 0
        #k가 0이 될때까지 반복문
        while k > 0:
            k -= self.fibonacci(k,[1,2])
            ans += 1
        return ans