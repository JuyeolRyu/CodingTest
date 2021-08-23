from collections import defaultdict
from collections import deque
def solution(n, edge):
    def bfs(start):
        visited = set([start])
        q = deque()
        q.append([start,0])
        while q:
            cur_node,depth = q.popleft()
            ans.append(depth)
                
            for node in graph[cur_node]:
                if node not in visited:
                    q.append([node,depth+1])
                    visited.add(node)

        return

    ans = []
    graph = defaultdict(list)
    
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    bfs(1)
    ans = list(reversed(ans))
    return ans.index(ans[0]-1)