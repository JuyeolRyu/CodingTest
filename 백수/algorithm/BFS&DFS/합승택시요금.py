import heapq
from collections import defaultdict
INF = float('inf')
def dijk(start,graph):
    dist = defaultdict(int)
    for node in graph:
        dist[node] = INF
    dist[start] = 0
    q = []
    heapq.heappush(q,[0,start])
    while q:
        cur_cost,cur_node = heapq.heappop(q)
        for ne_node,ne_cost in graph[cur_node]:
            cost = cur_cost+ne_cost
            if cost < dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(q,[cost,ne_node])
    return dist
def solution(n, s, a, b, fares):
    answer = INF
    graph = defaultdict(list)
    for c,d,cost in fares:
        graph[c].append([d,cost])
        graph[d].append([c,cost])
    
    way_points = dijk(s,graph)
    for node in way_points:
        end_points = dijk(node,graph)
        cost = way_points[node]+end_points[a]+end_points[b]
        answer = min(cost,answer)
    return answer