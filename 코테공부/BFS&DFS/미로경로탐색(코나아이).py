import copy

def dfs(current_node, graph, path ,check):
  row, col = current_node
  max_len = 0

  #깊은복사
  tmp_path = copy.deepcopy(path)
  tmp_graph = copy.deepcopy(graph)

  #범위 벗어난 경우
  if row < 0 or row >= len(graph) or col < 0 or col >= len(graph[0]):
    return len(path)
  
  #한번 방문했던 노드인 경우
  if graph[row][col].isdigit():
    return len(path)

  if ord( graph[row][col] ) == ord(path[-1]): #현재 노드와 이전 노드가 같은 알파벳인 경우
    return len(path)
  elif ord( graph[row][col] ) < ord(path[-1]):#이전 노드의 값이 더 큰 경우
    if check:                                 #한번의 예외 사용한 경우
      return len(path)
    else:                                     #한번의 예외
      check = True
      tmp_path.append(graph[row][col])

      tmp_graph[row][col] = '0'
      max_len = max( dfs([row-1,col],tmp_graph,tmp_path,check), max_len )
      max_len = max( dfs([row+1,col],tmp_graph,tmp_path,check), max_len )
      max_len = max( dfs([row,col-1],tmp_graph,tmp_path,check), max_len )
      max_len = max( dfs([row,col+1],tmp_graph,tmp_path,check), max_len )
  elif ord( graph[row][col] ) > ord(path[-1]):#갈수 있는 경우
    tmp_path.append(graph[row][col])
    tmp_graph[row][col] = '0'
    max_len = max( dfs([row-1,col],tmp_graph,tmp_path,check), max_len )
    max_len = max( dfs([row+1,col],tmp_graph,tmp_path,check), max_len )
    max_len = max( dfs([row,col-1],tmp_graph,tmp_path,check), max_len )
    max_len = max( dfs([row,col+1],tmp_graph,tmp_path,check), max_len )

  return max_len #가장 멀리까지 간 길이 반환
##########################################################################################

graph = []
ans = 0
for i in range(5):
  graph.append(list(input()))

#시작점이 어디인지 모르니까 모든 지점에서 전부 시작해봄 
for row in range(len(graph)):
  for col in range(len(graph[0])):
    tmp = graph[row][col]
    graph[row][col] = '0'
    ans = max( dfs( [row-1,col], graph, [tmp], False), ans )
    ans = max( dfs([row+1,col], graph, [tmp], False), ans )
    ans = max( dfs([row,col-1], graph, [tmp], False), ans )
    ans = max( dfs([row,col+1], graph, [tmp], False), ans )

print(ans)