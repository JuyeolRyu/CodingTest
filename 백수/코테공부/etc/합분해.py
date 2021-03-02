#https://www.acmicpc.net/problem/2225
from math import factorial
n,k=map(int,input().split())
dp = [0 for i in range(n+1)]
print((factorial(n+k-1)//(factorial(n)*factorial(k-1)))%1000000000)