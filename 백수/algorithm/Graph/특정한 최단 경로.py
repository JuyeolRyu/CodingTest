#특정한 최단 경로
#https://www.acmicpc.net/problem/1504

#sol1(다익스트라)
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def dijk(g,s):
    #distance dictionary init
    dist = defaultdict(int)
    for node in g:
        dist[node] = float('inf')
    dist[s] = 0
    q = []
    heapq.heappush(q,[dist[s],s])

    while q:
        cur_cost,cur_node = heapq.heappop(q)
        if dist[cur_node] < cur_cost:
            continue
        for ne_node,ne_cost in g[cur_node]:
            cost = cur_cost+ne_cost
            if cost < dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(q,[cost,ne_node])
    return dist
        
#input value
n,e = map(int,input().split())
graph = defaultdict(list)

for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

pre_node1,pre_node2 = map(int,input().split())
one_to_other = dijk(graph,1)
pre1_to_other = dijk(graph,pre_node1)
pre2_to_other = dijk(graph,pre_node2)

ans1 = one_to_other[pre_node1]+pre1_to_other[pre_node2]+pre2_to_other[n]
ans2 = one_to_other[pre_node2]+pre2_to_other[pre_node1]+pre1_to_other[n]

if (ans1 == float('inf') or ans1 == 0) and (ans2 == float('inf') or ans2 == 0):
    print(-1)
elif (ans1 == float('inf') or ans1 == 0):
    print(ans2)
elif (ans2 == float('inf') or ans2 == 0):
    print(ans1)
else:
    print(min(ans1,ans2))

'''
4 5
1 2 10
1 3 11
2 3 20
2 4 30
3 4 100
2 3
'''