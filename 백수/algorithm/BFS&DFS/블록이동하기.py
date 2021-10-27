import sys
from collections import deque
from copy import deepcopy
MAX = sys.maxsize
sys.setrecursionlimit(10**6)
def solution(board):
    answer = 0
    move=[[-1,0,-1,0],[1,0,1,0],[0,-1,0,-1],[0,1,0,1],[1,1,0,0],[-1,1,0,0],[1,-1,0,0],[-1,-1,0,0],[0,0,-1,-1],[0,0,1,-1],[0,0,-1,1],[0,0,1,1]]
    visited=[]
    q=deque()
    q.append([[0,0],[0,1],0])
    n = len(board)
    
    def is_valid(cur_pointA,ne_pointA,pointB):
        point=[]
        if abs(pointB[0]-ne_pointA[0])+abs(pointB[1]-ne_pointA[1])>1:
            return False
        for nums in zip(*[cur_pointA,ne_pointA,pointB]):
            for num in nums:
                if nums.count(num)==1:
                    point.append(num)
                    break
        #print(point,n)
        if 0>point[0] or point[0]>=n or 0>point[1] or point[1]>=n or board[point[0]][point[1]]==1:
            return False
        #print('hello')
        return True

    
    while q:
        a,b,cnt=q.popleft()
        
        if a == [n-1,n-1] or b == [n-1,n-1]:
            return cnt
        visited.append(a+b)
        
        for i in range(4):
            nar,nac=a[0]+move[i][0],a[1]+move[i][1]
            nbr,nbc=b[0]+move[i][2],b[1]+move[i][3]
            
            if 0<=nar<n and 0<=nac<n and 0<=nbr<n and 0<=nbc<n and [nar,nac,nbr,nbc] not in visited and board[nar][nac]==0 and board[nbr][nbc]==0:
                q.append([[nar,nac],[nbr,nbc],cnt+1])
                
        for i in range(4,8):
            nar,nac=a[0]+move[i][0],a[1]+move[i][1]
            nbr,nbc=b[0]+move[i][2],b[1]+move[i][3]
            
            if 0<=nar<n and 0<=nac<n and 0<=nbr<n and 0<=nbc<n and [nar,nac,nbr,nbc] not in visited and is_valid(a,[nar,nac],[nbr,nbc]) and board[nar][nac]==0 and board[nbr][nbc]==0:
                q.append([[nar,nac],[nbr,nbc],cnt+1])
                
        for i in range(8,12):
            nar,nac=a[0]+move[i][0],a[1]+move[i][1]
            nbr,nbc=b[0]+move[i][2],b[1]+move[i][3]
            
            if 0<=nar<n and 0<=nac<n and 0<=nbr<n and 0<=nbc<n and [nar,nac,nbr,nbc] not in visited and is_valid(b,[nbr,nbc],[nar,nac]) and board[nar][nac]==0 and board[nbr][nbc]==0:
                q.append([[nar,nac],[nbr,nbc],cnt+1])
                

    return answer