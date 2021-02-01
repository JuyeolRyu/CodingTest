#################################################################
#121. Best Time to Buy and Sell Stock                           #
#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ #
#################################################################


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, ans = float('inf'), 0
        for p in prices:
            #최소가격 찾기
            buy = min(buy, p)
            #이전까지의 최대값 vs 현재가격 - 최소가격
            ans = max(ans, p-buy)
        return ans