#용액
#https://www.acmicpc.net/problem/2467

#sol1(two pointer)
import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int,input().split()))
left,right = 0,n-1
ans = [float('inf'),float('inf')]
while left<right:
    ans_sum = sum(ans)
    cur_sum = li[left]+li[right]
    if cur_sum == 0:
        ans = [li[left],li[right]]
        break
    if abs(cur_sum)<abs(ans_sum):
        ans = [li[left],li[right]]
    if cur_sum < 0:
        left+=1
    elif cur_sum > 0:
        right-=1
for a in ans:
    print(a,end=' ')