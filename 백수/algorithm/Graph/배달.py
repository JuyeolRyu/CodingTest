from collections import defaultdict
import heapq

def dijk(g,s):
    dist = defaultdict(int)
    for node in g:
        dist[node]=float('inf')
    dist[s] = 0
    
    q=[]
    heapq.heappush(q,[dist[s],s])
    
    while q:
        cur_cost,cur_node = heapq.heappop(q)
        for ne_node,ne_cost in g[cur_node]:
            cost = dist[cur_node]+ne_cost
            if cost<dist[ne_node]:
                dist[ne_node] = cost
                heapq.heappush(q,[cost,ne_node])
    return dist
    
def solution(N, road, K):
    answer = 0
    #make graph
    graph = defaultdict(list)
    for a,b,c in road:
        graph[a].append([b,c])
        graph[b].append([a,c]) 
    
    result = dijk(graph,1)
    for r in result:
        if result[r]<=K:
            answer+=1
    return answer