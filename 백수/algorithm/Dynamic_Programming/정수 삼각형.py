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

#https://programmers.co.kr/learn/courses/30/lessons/43105
def solution(t):
    dp = []
    for i in range(1,len(t)):
        dp = [0]*len(t[i])
        for j in range(len(t[i])):
            if j == 0:
                dp[j] = t[i][j]+t[i-1][j]
            elif j == len(t[i])-1:
                dp[j] = t[i][j]+t[i-1][j-1]
            else:
                dp[j] = max(dp[j], t[i][j]+t[i-1][j-1], t[i][j]+t[i-1][j])
                
        t[i] = dp

    return max(t[-1])