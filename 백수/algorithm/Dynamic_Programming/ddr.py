#Dance Dance Revolution
#https://www.acmicpc.net/problem/2342

#sol1(dp)
import sys
sys.setrecursionlimit(10*7)
input = sys.stdin.readline

def sol(l,r,idx):
    if idx == arr_len:
        return 0
    
    #이미 방문했으면
    if dp[idx][l][r] != -1:
        return dp[idx][l][r]

    left_cost = 0
    right_cost = 0

    if l == arr[idx]:
        left_cost= 1
    elif l == 0:
        left_cost= 2
    else:
        if abs(l-arr[idx]) != 2:
            left_cost= 3
        else:
            left_cost= 4

    if r == arr[idx]:
        right_cost= 1
    elif r == 0:
        right_cost= 2
    else:
        if abs(r-arr[idx]) != 2:
            right_cost= 3
        else:
            right_cost= 4

    dp[idx][l][r] = min(sol(arr[idx],r,idx+1)+left_cost, sol(l,arr[idx],idx+1)+right_cost)
    return dp[idx][l][r]
    
arr = list(map(int,input().split()))[:-1]
arr_len = len(arr)
dp = [[[-1]*5 for _ in range(5)] for _ in range(arr_len)]

print(sol(0,0,0))