################################################################################
#1518. Water Bottles                                                           #
#https://leetcode.com/problems/water-bottles/                                  #
################################################################################

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = 0
        left_bottles = 0
        while(True):
            #음료 마시기
            ans += numBottles
            left_bottles += numBottles
            
            if(left_bottles >= numExchange):
                numBottles = left_bottles //numExchange
                left_bottles = left_bottles % numExchange
            else:
                break

        return ans