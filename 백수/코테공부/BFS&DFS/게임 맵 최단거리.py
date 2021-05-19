#https://programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    dr=[-1,1,0,0]
    dc=[0,0,-1,1]
    dp = [[-1]*len(maps[0]) for _ in range(len(maps))]
    dp[0][0] = 1
    q = deque()
    q.append([0,0])
    
    while q:
        r,c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<len(maps) and 0<=nc<len(maps[0]) and maps[nr][nc] == 1 and dp[nr][nc] == -1:
                dp[nr][nc] = dp[r][c]+1
                q.append([nr,nc])
    return dp[-1][-1]