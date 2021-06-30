#탈출
#https://www.acmicpc.net/problem/3055

#sol1
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(200000)


n,m = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(n)]
que = deque()
userQ = deque()
dr = [-1,1,0,0]
dc = [0,0,-1,1]
end = []
ans = 0
#find start
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'S':
            userQ.append([0,r,c,0])
        elif grid[r][c] == '*':
            que.append([1,r,c,0])
        elif grid[r][c] == 'D':
            end= [r,c]

while userQ:
    que.append(userQ.popleft())
while que:
    isUser,row,col,depth = que.popleft()

    if isUser == 0 and row == end[0] and col == end[1]:
        ans = depth
        break

    for i in range(4):
        nr = row+dr[i]
        nc = col+dc[i]

        if 0<=nr<n and 0<=nc<m:
            if isUser == 0 and (grid[nr][nc]=='.' or grid[nr][nc]=='D'):
                grid[nr][nc] = 'S'
                que.append([0,nr,nc,depth+1])
            elif isUser == 1 and (grid[nr][nc]=='.' or grid[nr][nc]=='S'):
                grid[nr][nc] = '*'
                que.append([1,nr,nc,depth+1])

if ans == 0:
    print('KAKTUS')
else:
    print(ans)

'''
3 3
S..
.D.
...

'''