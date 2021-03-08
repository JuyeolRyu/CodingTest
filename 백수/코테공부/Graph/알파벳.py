#https://www.acmicpc.net/problem/1987
r,c = map(int,input().split())
grid = []
for row in range(r):
  grid.append(list(map(lambda x: ord(x)-65,input())))
visited = [0]*26
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(row,col,cnt):
  global ans
  ans = max(ans,cnt)
  for i in range(4):
    nr = row+dr[i]
    nc = col+dc[i]

    if 0<=nr<r and 0<=nc<c and visited[grid[nr][nc]] == 0:
      visited[grid[nr][nc]] = 1
      dfs(nr,nc,cnt+1)
      visited[grid[nr][nc]] = 0

ans = 1
visited[grid[0][0]] = 1
dfs(0,0,ans)
print(ans)
'''
4 4
aaaa
cdae
baad
fjkl

3 4
ABCD
BCDA
CDEF

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
'''