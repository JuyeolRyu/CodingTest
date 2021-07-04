################################################################################
#1403. Minimum Subsequence in Non-Increasing Order                             #
#https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/    #
################################################################################

#solution 1
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        #내림차순 정렬
        nums.sort(reverse = True)
        #인덱스 비교해가면서 앞의 리스트의 합이 더 커졌을때 반환
        for idx in range(len(nums)):
            f_list = nums[:idx+1]
            s_list = nums[idx+1:]
            if(sum(f_list) > sum(s_list)):
                return nums[:idx+1]

#solution 2
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        #내림차순 정렬 & 전체 리스트의 합
        nums.sort(reverse = True)
        sum_list = sum(nums)
        #sub_list 의 합과 전체 리스트의 합의 차를 비교하면서 진행
        for idx in range(len(nums)):
            sub_list = nums[:idx+1]
            sum_sub = sum(nums[:idx+1])
            if(sum_list - sum_sub < sum_sub):
                return sub_list
