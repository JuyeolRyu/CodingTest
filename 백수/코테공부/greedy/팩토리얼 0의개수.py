'''
팩토리얼 0의 개수
https://www.acmicpc.net/status?user_id=back2225&problem_id=1676&from_mine=1
'''
import sys
input = sys.stdin.readline
n = int(input())

#sol1
num = 1
ans = 0
for i in range(1,n+1):
  num *= i

for c in list(reversed(str(num))):
  if c == '0':
    ans +=1
  else:
    break
print(ans)

#sol2
ans = 0
i = 1
while 5**i <= n:
  i+=1

for num in range(1,n+1):
  for j in range(i-1,0,-1):
    if num % (5**j) == 0:
      ans += j
      break

print(ans)