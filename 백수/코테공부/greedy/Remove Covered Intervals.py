#################################################################
#1288. Remove Covered Intervals                                 #
#https://leetcode.com/problems/remove-covered-intervals/        #
#################################################################
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        #시작이 작은 값들을 기준으로 정렬, 그리고 같은 값인 경우 뒤자리가 큰 순서대로 정렬
        intervals = sorted(intervals, key = lambda x: (x[0],-x[1]))
        ans = len(intervals)
        min_val,max_val = intervals.pop(0)
        
        for interval in intervals:
            #현재 뒷자리가 더 크면 범위가 포함 되므로 -1
            #아닌 경우 max값 교체
            if(interval[1] <= max_val):
                ans-=1
            else:
                max_val = interval[1]

        return ans
            