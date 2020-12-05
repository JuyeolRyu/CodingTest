################################################################################
#944. Delete Columns to Make Sorted                                            #
#https://leetcode.com/problems/delete-columns-to-make-sorted/                  #
################################################################################
#쓰레기 문제
class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        even = 0
        odd = 0
        for num in position:
            if(num % 2 == 0):
                even += 1
            else:
                odd += 1
        
        return(min(even,odd))