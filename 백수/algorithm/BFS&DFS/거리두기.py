from collections import deque
dr = [-1,1,0,0]
dc = [0,0,-1,1]

def bfs(place,r,c):
    que = deque()
    que.append([r,c,0])
    visited = [[0 for y in range(5)] for x in range(5)]
    visited[r][c] = 1
    
    while que:
        r,c,depth = que.popleft()
        if 1<=depth<=2 and place[r][c] == 'P':
            return False
        if depth >= 3:
            break
        
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<5 and 0<=nc<5:
                if place[nr][nc] != 'X' and visited[nr][nc] == 0:
                    que.append([nr,nc,depth+1])
                    visited[nr][nc] = 1
                
    return True

def solution(places):
    answer = []

    for place in places:
        check = True

        for r in range(len(place)):
            for c in range(len(place[0])):
                if place[r][c] == 'P':
                    if not bfs(place,r,c):
                        check = False
                        break
            if not check:
                break
        if check:
            answer.append(1)
        else:
            answer.append(0)

    return answer