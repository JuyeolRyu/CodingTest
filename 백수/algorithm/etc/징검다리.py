#https://programmers.co.kr/learn/courses/30/lessons/43236
from itertools import combinations
def solution(d, rocks, n):
    ans = 0
    rocks.sort()
    left,right = 0,d
    while left<=right:
        mid = (left+right)//2
        min_dist = float('inf')
        cur = 0
        remove_cnt = 0
        for rock in rocks:
            if rock-cur < mid:
                remove_cnt += 1
            else:
                min_dist = min(min_dist,rock-cur)
                cur = rock
        if remove_cnt > n:
            right = mid-1
        else:
            ans = max(ans,min_dist)
            left = mid+1
    return ans