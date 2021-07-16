#세 용액
#https://www.acmicpc.net/problem/2473

#sol1(two pointer)
import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int,input().split()))
li.sort()
ans = [float('inf'),[0,0,0]]

for left in range(n-2):
    check = False
    mid,right = left+1,n-1

    while mid<right:
        cur_sum = li[left]+li[mid]+li[right]

        if abs(cur_sum)<abs(ans[0]):
            ans = [cur_sum,[left,mid,right]]

        if cur_sum<0:
            mid+=1
        elif cur_sum>0:
            right-=1
        else:
            check = True
            break
    if check:
        break

for i in ans[1]:
    print(li[i],end=' ')