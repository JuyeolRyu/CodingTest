##########################################################################################
#욕심쟁이 판다                                                                            #
#https://www.acmicpc.net/problem/1937                                                    #
##########################################################################################
def dfs(current_node):
  row, col = current_node

  #방문한 적이 없는 노드만 방문한다
  if visited[row][col] < 0:
    #값을 0으로 만들어서 방문 표시
    visited[row][col] = 0
    #4방향 모두 확인
    for i in range(4):
      n_row, n_col = row + d_row[i], col + d_col[i]
      
      #이번에 방문할 노드가 그래프 범위 내라면
      if 0<= n_row < n and 0<= n_col <n :
        #이전 그래프 값보다 더 클 경우만 넘어가는 조건
        if graph[row][col] < graph[n_row][n_col]:
          visited[row][col] = max(visited[row][col], dfs([n_row,n_col]))
    
    visited[row][col] += 1
  return visited[row][col]
##########################################################################################
ans = 0
graph = []
#값 입력 받기
n = int(input())
for i in range(n):
  graph.append(list(map(int,input().split())))
#방문한 노드를 확인하기 위해 visited list 생성
visited = [[-1] * n for _ in range(n)]
#상하좌우 확인용 리스트
d_row = [-1,1,0,0]
d_col = [0,0,-1,1]

#시작점이 어디인지 모르니까 모든 지점에서 전부 시작해봄 
for row in range(len(graph)):
  for col in range(len(graph[0])):
    ans = max(ans, dfs( [row, col] ) )

print(ans)