#수 찾기
#https://www.acmicpc.net/problem/1920

#sol1 in 연산자 사용
import sys
input = sys.stdin.readline

ans = 0
n = int(input())
n_li = list(map(int,input().split()))
m = int(input())
m_li = list(map(int,input().split()))

for mn in m_li:
    if mn in n_li:
        print(1)
    else:
        print(0)

#sol2 이분탐색 사용(빠름)
import sys
input = sys.stdin.readline

def binary_search(li,left,right,n):
    mid = (left+right)//2
    if left == right:
        if li[left] == n:
            return 1
        else:
            return 0

    if li[mid] < n:
        return binary_search(li,mid+1,right,n)
    else:
        return binary_search(li,left,mid,n)
ans = 0
n = int(input())
n_li = list(map(int,input().split()))
m = int(input())
m_li = list(map(int,input().split()))
n_li.sort()

for mn in m_li:
    print(binary_search(n_li,0,n-1,mn))