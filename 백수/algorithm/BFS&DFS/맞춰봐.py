#맞춰봐
#https://www.acmicpc.net/problem/1248

#sol1(dfs)
import sys
input = sys.stdin.readline

def is_posiible(idx):
    tmp = 0
    for i in range(idx,-1,-1):
        tmp += ans[i]
        if arr[i][idx] == '-' and tmp >= 0:
            return False
        elif arr[i][idx] == '+' and tmp <=0:
            return False
        elif arr[i][idx] == '0' and tmp!=0:
            return False

    return True

def dfs(idx):
    if idx == N:
        print(" ".join(map(str,ans)))
        exit(0)

    for i in range(-10,11):
        ans.append(i)
        if is_posiible(idx):
            dfs(idx+1)
        ans.pop()
    return

N = int(input())
S = input().rstrip()
ans = []
arr = [[0]*N for _ in range(N)]

idx = 0
for i in range(N):
    for j in range(i,N):
        arr[i][j] = S[idx]
        idx+=1
dfs(0)