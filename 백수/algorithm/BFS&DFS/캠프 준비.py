#캠프준비
#https://www.acmicpc.net/problem/16938

#sol1(dfs)
import sys
input = sys.stdin.readline

def dfs(min_score,max_score,sum_score,idx,depth):
    global ans
    if depth >= 2:
        if l<=sum_score<=r and max_score-min_score >= x:
            ans += 1
    
    for i in range(idx,n):
        if sum_score+A[i]<=r:
            dfs(min(min_score,A[i]),max(max_score,A[i]),sum_score+A[i],i+1,depth+1)


ans = 0
n,l,r,x = map(int,input().split())
A = list(map(int,input().split()))
dfs(float('inf'),-float('inf'),0,0,0)
print(ans)


'''
3 5 6 1
1 2 3
'''