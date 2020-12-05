##########################################################################################
#435. Non-overlapping Intervals                                                          #
#https://leetcode.com/problems/non-overlapping-intervals/                                #
##########################################################################################

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #끝자리 수를 기준으로 오름차순 정렬
        intervals = sorted(intervals, key = lambda x:x[1] )
        ans = 0
        #빈 리스트가 입력될 경우 예외처리
        if not intervals:
            return ans

        #리스트 첫번째 값만 빼줌
        prev_s, prev_e = intervals.pop(0)

        for interval in intervals:
            #이전 끝자리 값보다 현재 시작값이 더 작으면 겹치므로 ans+1  
            if interval[0] < prev_e:
               ans += 1
            #겹치지 않는 경우 이전 시작,끝 값 갱신
            else:
                prev_s ,prev_e = interval
            
        return ans