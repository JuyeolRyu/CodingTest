############################################################################
#53. Maximum Subarray                                                      #
#https://leetcode.com/problems/maximum-subarray/                           #
############################################################################

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #nums와 같은 크기의 리스트를 만들어준다
        dp = [-float('inf') for _ in range(len(nums))]

        for idx in range(len(nums)):
            #첫번째 인덱스의 경우 nums[0]을 dp에 넣어준다
            if idx == 0:
                dp[idx] = nums[idx]
                continue
            #이전 값들의 합 최대값 + 현재값, 현재값 중 더 큰수를 고른다
            dp[idx] = max(dp[idx-1] + nums[idx], nums[idx])
            
        return max(dp)