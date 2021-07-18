#소수의 연속합
#https://www.acmicpc.net/problem/1644

#sol1(dp)
import sys
input = sys.stdin.readline

def find_prime(num):
    ret = [True]*(num)
    m = int(num**0.5)
    for i in range(2,m+1):
        if ret[i]:
            for j in range(i+i,num,i):
                ret[j] = False

    return [i for i in range(2,n+1) if ret[i]]
n = int(input())
dp = [i for i in range(n+1)]
prime_nums = find_prime(n+1)
ans = 0
left,right = -1,0
while right<len(prime_nums) and left<=right:
    if dp[prime_nums[right]] > n:
        left += 1
        dp[prime_nums[right]] -= prime_nums[left]
    elif dp[prime_nums[right]] < n:
        right+=1
        if right>=len(prime_nums):
            break
        dp[prime_nums[right]]+=dp[prime_nums[right-1]]
    else:
        ans += 1
        right+=1
        if right>=len(prime_nums):
            break
        dp[prime_nums[right]]+=dp[prime_nums[right-1]]

print(ans)