############################################################################
#491. Increasing Subsequences                                              #
#https://leetcode.com/problems/increasing-subsequences/                    #
############################################################################
#sol1 backtracking
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(curr, nums):
            #길이가 2이상이고 이전 값이 현재 값보다 큰경우 성립X이므로 반환
            if len(curr) >= 2 and curr[-1] < curr[-2]:
                return
            #현재 만들어진 subsequence가 결과에 없으면 추가해준다
            if len(curr) >= 2 and curr[:] not in result:
                result.add(curr[:])
            #현재 값을 subsequence에 추가하고 nums는 다음값부터 backtracking에 넣는다
            for i in range(len(nums)):
                backtrack( curr + (nums[i],), nums[i+1:] )
        
        result = set()
        backtrack( (), nums)
        return result

#sol2
'''
class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums: return nums
        curr = [[nums[0]]]
        for x in nums[1:]:
            curr += [y+[x] for y in curr if x>=y[-1]]
            curr += [[x]]
        curr = [tuple(x) for x in curr if len(x)>=2]
        return list(set(curr))
'''