#https://programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque
def solution(board):
    blen = len(board)
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    dp = [[float('inf')]*blen for _ in range(blen)]
    dp[0][0] = 0
    q = deque()
    q.append([0,0,0,-1])
    while q:
        r,c,cost,direction = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<blen and 0<=nc<blen and board[nr][nc] == 0:
                if direction == i or direction == -1:
                    ncost=cost+100
                else:
                    ncost=cost+600
                    
                if dp[nr][nc]>=ncost:
                    dp[nr][nc] = ncost
                    q.append([nr,nc,ncost,i])

    return dp[-1][-1]