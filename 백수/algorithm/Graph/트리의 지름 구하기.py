#트리의 지름
#https://www.acmicpc.net/problem/1967

#sol1
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijk(graph,start):
    dist = defaultdict(int)
    for node in graph:
        dist[node] = float('inf')
    dist[start] = 0
    q = [[dist[start],start]]
    while q:
        cur_cost,cur_node = heapq.heappop(q)
        for ne_node,ne_cost in graph[cur_node]:
            cost = dist[cur_node]+ne_cost
            if cost < dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(q,[cost,ne_node])
    return dist
n = int(input())
graph = defaultdict(list)
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

first_node = sorted(dijk(graph,1).items(), key = lambda x:x[1],reverse=True)[0]
second_node = sorted(dijk(graph,first_node[0]).items(), key = lambda x:x[1],reverse=True)[0]

print(second_node[1])