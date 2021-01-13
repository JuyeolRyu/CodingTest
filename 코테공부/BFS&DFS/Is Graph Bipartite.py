#https://leetcode.com/problems/is-graph-bipartite/
#785. Is Graph Bipartite?
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors = dict()
        
        def dfs(vertice,color):
            colors[vertice] = color
            #다음 노드 방문
            for to_vertice in graph[vertice]:
                #방문한적이 있는 노드
                if to_vertice in colors:
                    #현재 노드와 이전 노드가 연결되있으면
                    if colors[to_vertice] == colors[vertice]:
                        return False
                #방문한적 없는 노드
                else:
                    #연결X
                    if not dfs(to_vertice,color*-1):
                        return False
            
            return True
        
        for vertice in range(len(graph)):
            if vertice not in colors and not dfs(vertice,1):
                return False
                
        return True