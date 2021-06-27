#https://www.acmicpc.net/problem/5014
import sys
from collections import deque
input = sys.stdin.readline

ans = 0
l,s,e,u,d = map(int,input().split())
#l층, 타겟:e층, 현재:s층
building = [float('inf')]*(l+1)
building[s] = 0
q = deque()
q.append(s)
while q:
    cur = q.popleft()
    if cur == e:
        break

    if cur+u<=l and building[cur]+1<building[cur+u]:
        building[cur+u] = building[cur]+1
        q.append(cur+u)
    if cur-d>0 and building[cur]+1<building[cur-d]:
        building[cur-d] = building[cur]+1
        q.append(cur-d)
if building[e] == float('inf'):
    print("use the stairs")
else:
    print(building[e])