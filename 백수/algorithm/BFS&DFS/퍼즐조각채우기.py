import copy
dr = [-1,1,0,0]
dc = [0,0,-1,1]
grid = []
def dfs(r,c,pos,check_num):
    global board
    ret = [pos]
    for i in range(4):
        nr = r+dr[i]
        nc = c+dc[i]
        if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == check_num:
            grid[nr][nc] = 2
            ret = ret+dfs(nr,nc,[pos[0]+dr[i],pos[1]+dc[i]],check_num)
            
    return ret
def rotate_90(li):
    N = len(li)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = li[r][c]
    return ret

def solution(game_board, table):
    global grid
    
    answer = 0
    block_set = []
    
    grid = game_board
    for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    grid[row][col] = 2
                    ret = dfs(row,col,[0,0],0)[1:]
                    block_set.append(ret)
                        
    for i in range(4):
        table = rotate_90(table)
        grid = copy.deepcopy(table)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    ret = dfs(row,col,[0,0],1)[1:]
                    if ret in block_set:
                        block_set.pop(block_set.index(ret))
                        answer += len(ret)+1
                        table = copy.deepcopy(grid)
                    else:
                        grid = copy.deepcopy(table)
        
    return answer