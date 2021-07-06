#최소비용 구하기
#https://www.acmicpc.net/problem/1916

#sol1(다익스트라)
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
def dijk(g,s):
    #make distance dictionary and init
    dist = defaultdict(int)
    for node in range(1,n+1):
        dist[node] = float('inf')
    dist[s] = 0

    #search dist
    q = []
    heapq.heappush(q,[dist[s],s])
    while q:
        cur_cost,cur_node = heapq.heappop(q)

        for ne_node,ne_cost in g[cur_node]:
            cost = dist[cur_node]+ne_cost
            if cost < dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(q,[cost,ne_node])
    return dist

#input value
n = int(input())
m = int(input())
graph = defaultdict(list)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

start,end = map(int,input().split())
ans = dijk(graph,start)

print(ans[end])