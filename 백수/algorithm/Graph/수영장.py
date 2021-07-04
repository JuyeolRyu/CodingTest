#https://www.acmicpc.net/problem/1113
import collections


def start(h):
    ret = 0
    for i in range(N):
        for j in range(M):
            if area[i][j] and area[i][j] < h and not visited[i][j]:
                ret += bfs(i, j, h)
    return ret

def bfs(i, j, h):
    q = collections.deque()
    pos = [[i, j]]
    q.append([i, j])
    visited[i][j] = True
    flag = False

    #bfs 탐색
    while q:
        i, j = q.popleft()
        for a in range(4):
            ni, nj = i+di[a], j+dj[a]
            #범위 안이고 
            if 0 <= ni < N and 0 <= nj < M and area[ni][nj]!=0:
              #방문한적 없는 노드
                if not visited[ni][nj]:
                    if area[ni][nj] < h:
                        visited[ni][nj] = True
                        pos.append([ni, nj])
                        q.append([ni, nj])
            else:
                flag = True

    if flag:
        return 0
    else:
        water = 0
        for i, j in pos:
            area[i][j] += 1
            water += 1
        return water

#입력
N, M = map(int, input().split())
area = [list(map(int, list(input()))) for _ in range(N)]
#상하좌우
di = [0, 0, -1, 1]
dj = [-1, 1, 0, 0]
result = 0
#물의 높이마다 탐색
for h in range(1, 10):
    visited = [[False] * M for _ in range(N)]
    result += start(h)
print(result)
'''
4 7
1666661
5362216
6616136
6666666

5 7
1666661
5362216
6616136
6666666
7777777


'''