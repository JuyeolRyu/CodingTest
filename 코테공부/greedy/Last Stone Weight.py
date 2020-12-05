################################################################################
#1046. Last Stone Weight                                                       #
#https://leetcode.com/problems/last-stone-weight/                              #
################################################################################

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse = True)

        while(len(stones) > 1):
            f_stone = stones.pop(0)
            s_stone = stones.pop(0)
            
            if(f_stone != s_stone):
                stones.append(f_stone - s_stone)
            
            stones.sort(reverse = True)

        if(len(stones) == 1):
            return stones[0]
        else:
            return 0