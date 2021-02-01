############################################################################
#303. Range Sum Query - Immutable                                          #
#https://leetcode.com/problems/range-sum-query-immutable/                  #
############################################################################

#sol1 그냥 풀기
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
    def sumRange(self, i: int, j: int) -> int:
        ans = 0
        #주어진 인덱스 범위만큼 반복문 돌아서 합을 구한다.
        for idx in range(i,j+1):
            ans += self.nums[idx]
        return ans
    
#sol2 dynamic programing
class NumArray:
    def __init__(self, nums: List[int]):
        self.dp = [nums[0] for _ in range(len(nums))]
        #0 ~ 해당 인덱스 까지의 합을 구한다.
        for idx in range(1,len(nums)):
            self.dp[idx] = self.dp[idx-1] + nums[idx]
            
    def sumRange(self, i: int, j: int) -> int:
        #처음 부터 시작인 경우 인덱스가 j일 경우를 반환하면 된다
        if i == 0:
            return self.dp[j]
        #그 외의 경우 j번째 - (i-1)번째 를 빼면 i~j 범위 까지의 합이 나온다
        return self.dp[j] - self.dp[i-1]