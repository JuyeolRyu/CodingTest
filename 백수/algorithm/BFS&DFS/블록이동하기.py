from collections import deque

def solution(board):
    answer = 0
    n=len(board)
    visited=set()
    visited.add(((1,1),(1,2)))
    q=deque()
    q.append([(1,1),(1,2),0])
    
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for r in range(n):
        for c in range(n):
            new_board[r+1][c+1]=board[r][c]
    

    def can_move(cur1, cur2):
        Y, X = 0, 1
        cand = []
        
        DELTAS = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for dy, dx in DELTAS:
            nxt1 = (cur1[Y] + dy, cur1[X] + dx)
            nxt2 = (cur2[Y] + dy, cur2[X] + dx)
            if new_board[nxt1[Y]][nxt1[X]] == 0 and new_board[nxt2[Y]][nxt2[X]] == 0:
                cand.append((nxt1, nxt2))

        if cur1[Y] == cur2[Y]:
            UP, DOWN = -1, 1
            for d in [UP, DOWN]:
                if new_board[cur1[Y]+d][cur1[X]] == 0 and new_board[cur2[Y]+d][cur2[X]] == 0:
                    cand.append((cur1, (cur1[Y]+d, cur1[X])))
                    cand.append((cur2, (cur2[Y]+d, cur2[X])))
        else:
            LEFT, RIGHT = -1, 1
            for d in [LEFT, RIGHT]:
                if new_board[cur1[Y]][cur1[X]+d] == 0 and new_board[cur2[Y]][cur2[X]+d] == 0:
                    cand.append(((cur1[Y], cur1[X]+d), cur1))
                    cand.append(((cur2[Y], cur2[X]+d), cur2))
        return cand
    
    while q:
        a,b,cnt=q.popleft()
        if a == (n,n) or b == (n,n):
            return cnt

        for ne in can_move(a,b):
            if ne not in visited:
                q.append([*ne,cnt+1])
                visited.add(ne)
                

    return answer