import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = []
dic = defaultdict(int)
for _ in range(n):
    tmp = int(input())
    nums.append(tmp)
    dic[tmp] += 1

nums.sort()
dic = sorted(dic.items(),key = lambda x:(-x[1],x[0]))
print(round(sum(nums) / n))
print(nums[n//2])
if len(dic) > 1 and dic[0][1] == dic[1][1]:
    print(dic[1][0])
else:
    print(dic[0][0])
print(nums[-1]-nums[0])