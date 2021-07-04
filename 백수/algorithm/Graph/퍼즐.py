#퍼즐
#https://www.acmicpc.net/problem/1525

#sol1
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs():
#     que = deque()
#     que.append(new_grid)
#     visited[new_grid] = 0

#     while que:
#         num = que.popleft()

#         if num == 123456789:
#             return visited[num]

#         s = str(num)
#         idx = s.find('9')
#         r,c = idx//3, idx%3

#         for i in range(4):
#             nr = r+dr[i]
#             nc = c+dc[i]

#             if 0<=nr<3 and 0<=nc<3:
#                 t = r*3+c
#                 ts = list(s)
#                 ts[idx], ts[t] = ts[t],ts[idx]
#                 ti = int("".join(ts))

#                 if not visited.get(ti):
#                     visited[ti] = visited[num]+1
#                     que.append(ti)
#     return -1

# dr = [-1,1,0,0]
# dc = [0,0,-1,1]
# visited = dict()
# grid = ""

# for _ in range(3):
#     grid += "".join(input().split())
# new_grid = int(grid.replace('0','9'))
# print(new_grid)
# print(bfs())

from collections import deque
def bfs(): 
    q = deque() 
    q.append(aa) 
    visited[aa] = 0 
    while q: 
        v = q.popleft() 
        if v == 123456789: 
            return visited[v] 
        s = str(v) 
        target = s.find('9') 
        tx = target // 3 
        ty = target % 3
        
        for i in range(4): 
            x = dx[i] + tx 
            y = dy[i] + ty 
            if 0 <= x < 3 and 0 <= y < 3: 
                t = x*3 + y 
                ts = list(s) 
                ts[target], ts[t] = ts[t], ts[target]
                ti = int(''.join(ts)) 
                if not visited.get(ti): 
                    visited[ti] = visited[v] + 1 
                    q.append(ti) 
    return -1 
    
dx = [1, -1, 0, 0] 
dy = [0, 0, 1, -1] 
visited = dict() 
aa = '' 
for i in range(3): 
    a = input() 
    a = a.replace(' ', '')
    aa += a
aa = int(aa.replace('0', '9')) 
print(bfs())
