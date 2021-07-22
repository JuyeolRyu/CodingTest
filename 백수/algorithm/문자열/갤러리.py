#갤러리
#https://www.acmicpc.net/problem/2115

#sol1(문자열)
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
grid = [list(input().rstrip()) for _ in range(N)]
wall = [[[0,0,0,0] for j in range(M)] for i in range(N)]
ans = 0

for i in range(1,N-1):
    for j in range(1,M-2):
        if grid[i][j]=="." and grid[i][j+1]==".":
            # 위쪽
            if grid[i-1][j]=="X" and grid[i-1][j+1]=="X" and wall[i][j][0]==0 and wall[i][j+1][0]==0:
                ans+=1
                wall[i][j][0]=wall[i][j+1][0]=1
            # 아래쪽
            if grid[i+1][j]=="X" and grid[i+1][j+1]=="X" and wall[i][j][2]==0 and wall[i][j+1][2]==0:
                ans+=1
                wall[i][j][2]=wall[i][j+1][2]=1

for j in range(1,M-1):
    for i in range(1,N-2):
        if grid[i][j]=="." and grid[i+1][j]==".":
            # 왼쪽
            if grid[i][j-1]=="X" and grid[i+1][j-1]=="X" and wall[i][j][1]==0 and wall[i+1][j][1]==0:
                ans+=1
                wall[i][j][1]=wall[i+1][j][1]=1
            # 오른쪽
            if grid[i][j+1]=="X" and grid[i+1][j+1]=="X" and wall[i][j][3]==0 and wall[i+1][j][3]==0:
                ans+=1
                wall[i][j][3]=wall[i+1][j][3]=1
print(ans)