from collections import defaultdict
def dfs(graph,visited,node):
    ret = 1
    for ne_node in graph[node]:
        if ne_node not in visited:
            visited.append(ne_node)
            ret+=dfs(graph,visited,ne_node)
    return ret
def solution(n, wires):
    answer = float('inf')
    graph = defaultdict(list)
    for s,e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    for node1 in graph:
        for node2 in graph[node1]:
            case1=dfs(graph,[node1,node2],node1)
            case2=dfs(graph,[node1,node2],node2)
            answer = min(answer,abs(case1-case2))
    return answer