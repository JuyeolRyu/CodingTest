#신기한 소수
#https://www.acmicpc.net/problem/2023

#sol1(dfs)
import sys
input = sys.stdin.readline

def is_prime(num):
    i = 2
    while i<=(num**0.5):
        if num%i == 0:
            return False
        else:
            i+=1
    return True

def dfs(prev,depth):
    if depth == n:
        ans.append(int(prev))
        return
    
    for i in range(9):
        if is_prime(int(prev+prime_list[i])):
            dfs(prev+prime_list[i],depth+1)
    return


ans = []
n = int(input())
prime_list = [str(i) for i in range(1,10)]
for i in ['2','3','5','7']:
    dfs(i,1)
ans.sort()
for a in ans:
    print(a)