#부분합
#https://www.acmicpc.net/problem/1806

#sol1(two points)
import sys
input = sys.stdin.readline
n,s = map(int,input().split())
arr = list(map(int,input().split()))
sum_arr = [0]*(n+1)
for i in range(1,n+1):
    sum_arr[i] = sum_arr[i-1]+arr[i-1]

left,right = 0,1
ans = float('inf')

while left < n:
    if sum_arr[right]-sum_arr[left] >= s:
        if right-left < ans:
            ans = right-left
        left+=1
    else:
        if right < n:
            right+=1
        else:
            left += 1

if ans == float('inf'):
    ans = 0
print(ans)