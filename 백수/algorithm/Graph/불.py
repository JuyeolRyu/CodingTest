#불
#https://www.acmicpc.net/problem/4179

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
ans = 0
#find start
for r in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[r][c] == 'J':
            que.append([0,r,c,0])
        elif grid[r][c] == 'F':
            que.append([1,r,c,0])

while que:
    isUser,row,col,depth = que.popleft()

    if (row == 0 or row == n-1 or col == 0 or col == m-1) and isUser == 0 and grid[row][col] == 'J':
        ans = depth+1
        break

    for i in range(4):
        nr = row+dr[i]
        nc = col+dc[i]

        #가장자리 도착
        if 0<=nr<n and 0<=nc<m:
            if isUser == 0 and grid[nr][nc]=='.':
                grid[nr][nc] = 'J'
                que.append([0,nr,nc,depth+1])
            elif isUser == 1 and (grid[nr][nc]=='J' or grid[nr][nc]=='.'):
                grid[nr][nc] = 'F'
                que.append([1,nr,nc,depth+1])

if ans == 0:
    print('IMPOSSIBLE')
else:
    print(ans)

'''
4 6
######
......
#.J###
#F####

4 4
####
JF.#
#..#
#..#

4 4
###F
#J.#
#..#
#..#

5 5
....F
...J#
....#
....#
...#.

3 3
F.F
.J.
F.F

5 5
#####
#...#
#.J.#
#...#
#####

'''