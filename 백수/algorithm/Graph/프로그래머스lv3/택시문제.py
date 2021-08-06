import heapq
from collections import defaultdict

def dijk(graph,start):
    dist = defaultdict(int)
    for node in graph:
        dist[node] = float('inf')
        
    dist[start] = 0
    que = [[dist[start],start]]
    
    while que:
        cur_cost,cur_node = heapq.heappop(que)
        for ne_node,ne_cost in graph[cur_node]:
            cost = dist[cur_node]+ne_cost
            if cost < dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(que,[cost,ne_node])
                
    return dict(dist)
def solution(n, s, a, b, fares):
    answer = float('inf')
    graph = defaultdict(list)
    
    for x,y,c in fares:
        graph[x].append([y,c])
        graph[y].append([x,c])

    for start in range(1,n+1):
        d = dijk(graph,start)
        answer = min(answer,d[s]+d[a]+d[b])

    return answer