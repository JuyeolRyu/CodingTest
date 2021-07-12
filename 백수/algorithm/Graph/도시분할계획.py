#도시 분할 계획
#https://www.acmicpc.net/problem/1647

#sol1(kruskal)
'''
최소스패닝 트리 만들고 그 중 제일 긴 간선 제거
'''
import sys
input = sys.stdin.readline

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y


n,m=map(int,input().split())
parent = [i for i in range(n+1)]
graph = []

for _ in range(m):
    a,b,c = map(int,input().split()) 
    graph.append([c,a,b])

cost = 0
ans = []

graph.sort()
for c,u,v in graph:
    if find(u) != find(v):
        union(u,v)
        ans.append(c)
        cost += c
print(cost-ans.pop())