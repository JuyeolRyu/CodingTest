import copy
from itertools import permutations
from collections import defaultdict
from collections import deque

dr=[-1,1,0,0]
dc=[0,0,-1,1]
b=[]
def ctrl_move(r,c,i):
    global b
    cr, cc = r, c 
    while True: 
        nr = cr + dr[i]
        nc = cc + dc[i]
        if not (0<=nr<4 and 0<=nc<4): 
            return cr, cc 
        if b[nr][nc] != 0: 
            return nr, nc 
        cr = nr 
        cc = nc 

def bfs(s,e):
    q = deque()
    q.append([s[0],s[1],0])
    visited=set()

    while q:
        row,col,dist=q.popleft()
        if (row,col) in visited:
            continue
            
        visited.add((row,col))
        if row==e[0] and col==e[1]:
            return dist
        for i in range(4):
            nr=row+dr[i]
            nc=col+dc[i]
            if 0<=nr<4 and 0<=nc<4:
                q.append([nr,nc,dist+1])
            nr,nc=ctrl_move(row,col,i)
            q.append([nr,nc,dist+1])
    return -1
def solution(board, r, c):
    global b
    answer = float('inf')
    cards=defaultdict(list)
    for row in range(4):
        for col in range(4):
            if board[row][col]:
                cards[board[row][col]].append([row,col])
    
    for permutation in permutations(cards,len(cards)):
        b=copy.deepcopy(board)
        row,col=r,c
        dist=0
        for num in permutation:
            cur_to_card1=bfs([row,col],cards[num][0])
            cur_to_card2=bfs([row,col],cards[num][1])
            if cur_to_card1<cur_to_card2:
                dist+=cur_to_card1
                dist+=bfs(cards[num][0],cards[num][1])
                row,col=cards[num][1]
            else:
                dist+=cur_to_card2
                dist+=bfs(cards[num][1],cards[num][0])
                row,col=cards[num][0]
            b[cards[num][0][0]][cards[num][0][1]]=0
            b[cards[num][1][0]][cards[num][1][1]]=0
            dist+=2
        answer=min(answer,dist)
    return answer