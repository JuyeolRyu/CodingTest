#https://www.acmicpc.net/problem/1915

r,c = map(int,input().split())
grid = []
ans = 0
dp = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
  grid.append(list(input()))

for row in range(r):
  for col in range(c):
    if grid[row][col] == '1':
      if dp[row][col] == dp[row+1][col] == dp[row][col+1] != 0:
        dp[row+1][col+1] = dp[row][col]+1
      elif dp[row][col] == 0 or dp[row+1][col] == 0 or dp[row][col+1] == 0:
        dp[row+1][col+1] = 1
      else:
        dp[row+1][col+1] = min(dp[row][col],dp[row+1][col],dp[row][col+1])+1
  
  ans = max(dp[row+1]+[ans])

print(ans*ans)

for row in dp:
  print(row)

'''
5 5
11100
11110
11111
01111
00111

4 4
0100
0111
1111
0111

4 4
0100
0111
1111
0011

5 5
01010
01110
01010
11100
00101

5 5
11111
11111
11111
11111
11111

3 3
011
111
111
'''