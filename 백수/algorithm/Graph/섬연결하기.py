import sys
sys.setrecursionlimit(10**6)

def solution(n, graph):
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x,y):
        x=find(x)    
        y=find(y)

        if x>y:
            parent[x]=y
        else:
            parent[y]=x
            
    answer = 0
    graph = sorted(graph,key=lambda x:x[2])
    parent = [i for i in range(n+1)]
    
    while graph:
        u,v,cost = graph.pop(0)
        if find(u) == find(v):
            continue
        else:
            union(u,v)
            answer+=cost
    return answer