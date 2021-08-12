def solution(rows, columns, queries):
    answer = []
    grid = [[c+columns*r for c in range(1,columns+1)] for r in range(rows)]

    for q in queries:
        r1,c1,r2,c2 = q[0]-1,q[1]-1,q[2]-1,q[3]-1
        tmp = []
        tmp.extend(grid[r1][c1:c2+1])
        tmp.extend([grid[r][c2] for r in range(r1+1,r2+1)])
        tmp.extend(list(reversed(grid[r2][c1:c2])))
        tmp.extend([grid[r][c1] for r in range(r2-1,r1,-1)])
        answer.append(min(tmp))
        
        tmp = [tmp.pop()]+tmp
        for c in range(c1,c2+1):
            grid[r1][c]=tmp.pop(0)
        for r in range(r1+1,r2+1):
            grid[r][c2]=tmp.pop(0)
        for c in range(c2-1,c1-1,-1):
            grid[r2][c]=tmp.pop(0)
        for r in range(r2-1,r1,-1):
            grid[r][c1]=tmp.pop(0)
    return answer