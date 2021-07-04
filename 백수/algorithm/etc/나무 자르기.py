#나무 자르기
#https://www.acmicpc.net/problem/2805

#sol1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

def binary_search(li,target,left,right):
    global ans
    if left == right:
        return left
    mid = (left+right)//2
    tmp_sum = 0
    for num in li:
        if num<=mid:
            break
        tmp_sum += (num-mid)

    if tmp_sum < target:
        return binary_search(li,target,left,mid)
    else:
        if ans < mid or tmp_sum == target:
            ans = mid
        return binary_search(li,target,mid+1,right)

n,m = map(int,input().split())
tree = list(map(int,input().split()))
tree.sort(reverse=True)
ans = 0

binary_search(tree,m,0,tree[0])
print(ans)