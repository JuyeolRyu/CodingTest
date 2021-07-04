##########################################################
#창고의 개수 n, 창고마다 있는 식량 리스트 arr 입력         #
#연속된 창고를 털지 못하고 최소 1칸 털어진 창고만 털수 있다.#
##########################################################

#sol1 dp 2개 사용
n = int(input())
arr = list(map(int,input().split()))
#이전 창고를 방문한경우 1
#           방문X 경우 2
dp1 = [0]*n
dp2 = [0]*n
dp1[0] = 1
for i in range(1,n):
  dp1[i] = max(dp2[i-1] + arr[i], dp1[i])
  dp2[i] = dp1[i-1]

print(max(dp1[n-1],dp2[n-1]))

#sol2 dp 1개 사용
n = int(input())
arr = list(map(int,input().split()))

dp = [0]*n
dp[0] = arr[0]
dp[1] = max(arr[0],arr[1])

for i in range(2,n):
  dp[i] = max(dp[i-2] + arr[i], dp[i-1])

print(dp[n-1])
