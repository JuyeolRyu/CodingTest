def is_valid(queen,row):
    for r in range(row):
        if queen[row] == queen[r] or abs(queen[row]-queen[r]) == row-r:
            return False
    return True
def dfs(queen,row,n):
    cnt = 0
    if row == n:
        return 1
    
    for col in range(n):
        queen[row] = col
        
        if is_valid(queen,row):    
            cnt+=dfs(queen,row+1,n)
    return cnt
def solution(n):
    return dfs([0]*n,0,n)