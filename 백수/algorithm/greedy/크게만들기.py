#https://www.acmicpc.net/problem/2457
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
num = input().rstrip()
li = []
for i,n in enumerate(num):
  while li and li[-1]<n and K>0:
    li.pop(-1)
    K -= 1
  li.append(n)
li = "".join(li)
print(li[:len(li)-K])
'''시간초과
re_num = list(reversed(num))
for i in sorted(num)[:k]:
  re_num.remove(i)
print("".join(list(reversed(re_num))))
2911
'''
'''
6 2
391123
//output : 9123

6 2
436436
//output : 6436

7 3
7654321
//output : 7654

6 2
362514
//output : 6514
'''