################################################################################
#1296. Divide Array in Sets of K Consecutive Numbers                           #
#https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/  #
################################################################################

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        #예외처리
        if len(nums) % k != 0:
            return False
            
        dic = dict()
        
        for num in sorted(nums):
            if num in dic:
                dic[num] = dic[num] + 1
            else:
                dic[num] = 1

            
        while dic:
            num = next(iter(dic))

            for num in range( num, num + k ):
                if num not in dic:
                    return False
                
                dic[num] = dic[num] - 1
                
                if not dic[num]:
                    del(dic[num])
        return True        