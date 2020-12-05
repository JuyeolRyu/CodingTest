from collections import deque

def bfs(current_node, graph):
  d_row = [0,0,1,-1]
  d_col = [1,-1,0,0]
  queue = deque()
  queue.append(current_node)

  while queue:
    #현재 노드의 row, col
    row, col = queue.popleft()
    #상하좌우 갈수 있는지 판단
    for i in range(4):
      n_row = row + d_row[i]
      n_col = col + d_col[i]

      #벽이거나 범위 벗어난 경우
      if n_row < 0 or n_row >= len(graph) or n_col < 0 or n_col >= len(graph[0]) or graph[n_row][n_col] == 0:
        continue
      
      #갈수 있는 노드인 경우
      if graph[n_row][n_col] == 1:
        
        graph[n_row][n_col] = graph[row][col] + 1
        queue.append([n_row,n_col])
  
  return graph[-1][-1]

######################################################
n, m = map(int,input().split())
graph = []

for i in range(n):
  graph.append(list(map(int,input())))

print( bfs([0,0],graph) )