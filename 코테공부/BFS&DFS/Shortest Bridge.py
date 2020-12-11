############################################################################################
#934. Shortest Bridge                                                                      #
#https://leetcode.com/problems/shortest-bridge/                                            #
############################################################################################

from collections import deque
class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        ans = float('inf')
        #대륙1,2
        field1 = []
        field2 = []
        isFirst = True
        #4방향 저장
        d_row = [-1,1,0,0]
        d_col = [0,0,-1,1]
        #육지의 끝인지 판단
        def isEdge(row,col):
            for i in range(4):
                n_row = row + d_row[i]
                n_col = col + d_col[i]
                #육지의 끝인 경우
                if 0<=n_row<len(A) and 0<=n_col<len(A) and A[n_row][n_col] == 0:
                    return True
                
            return False
                
        #
        for row in range(len(A)):
            for col in range(len(A)):
                #육지라면
                if A[row][col] == 1:
                    #방문처리
                    A[row][col] = -1
                    queue = deque()
                    queue.append([row,col])
                    
                    #연결된 모든 대륙 탐사할때까지
                    while queue:
                        r,c = queue.popleft()
                        #첫번째 대륙이고 끝일 경우 edge에 추가
                        if isFirst and isEdge(r,c):
                            field1.append([r,c])
                        #두번째 대륙이고 끝일 경우 edge에 추가
                        else:
                            if isEdge(r,c):
                                field2.append([r,c])
                        #다음으로 갈곳 탐색
                        for i in range(4):
                            n_row = r + d_row[i]
                            n_col = c + d_col[i]
                            #범위 안이고 대륙일 경우
                            if 0<=n_row<len(A) and 0<=n_col<len(A) and A[n_row][n_col] == 1:
                                queue.append([n_row,n_col])
                                A[n_row][n_col] = -1
                    #다음 대륙으로
                    isFirst = False
        #각 대륙의 edge중 거리가 최소인것을 구한다
        for r1,c1 in field1:
            for r2,c2 in field2:
                ans = min(ans, abs(r2-r1) + abs(c2-c1) - 1)
                
        return ans