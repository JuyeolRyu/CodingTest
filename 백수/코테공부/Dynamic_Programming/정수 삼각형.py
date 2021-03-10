#https://www.acmicpc.net/problem/1932
n = int(input())
triangle = [list(map(int,input().split())) for i in range(n)]

for i in range(1,n):
  for j in range(len(triangle[i])):
    if j == 0:
      triangle[i][j] += triangle[i-1][0]
    elif j == len(triangle[i])-1:
      triangle[i][j] += triangle[i-1][j-1]
    else:
      triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
print(max(triangle[-1]))