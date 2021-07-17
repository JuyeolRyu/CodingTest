#별자리 만들기
#https://www.acmicpc.net/problem/4386

#sol1(dp)
import sys,math,heapq
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]
def union(x,y):
    x = find(x)
    y = find(y)

    if x >= y:
        parent[x] = y
    else:
        parent[y] = x

n = int(input())
node = [list(map(float,input().split())) for _ in range(n)]
graph = []
parent = [i for i in range(n)]
for i in range(n):
    for j in range(i+1,n):
        tmp = math.sqrt((node[i][0]-node[j][0])**2 + (node[i][1]-node[j][1])**2)
        heapq.heappush(graph,[tmp,i,j])
ans = 0
while graph:
    c,u,v = heapq.heappop(graph)
    if find(u) == find(v):
        continue
    else:
        union(u,v)
        ans += c
print(round(ans,2))