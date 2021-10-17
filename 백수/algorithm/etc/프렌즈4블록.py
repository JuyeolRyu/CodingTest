#https://programmers.co.kr/learn/courses/30/lessons/17679

def rotate(grid):
    return list(map(list,zip(*grid)))
def remove_block(board,n,m):
    remove_set=set()
    
    for row in range(n-1):
        for col in range(m-1):
            if board[row][col] != "" and board[row][col]==board[row+1][col]==board[row][col+1]==board[row+1][col+1]:
                remove_set.add((row,col))
                remove_set.add((row+1,col))
                remove_set.add((row,col+1))
                remove_set.add((row+1,col+1))
        
    for row,col in remove_set:
        board[row][col]=""
    for idx,row in enumerate(board):
        row="".join(row)
        board[idx]=[""]*(m-len(row))+list(row)
        
    return board,len(remove_set)
def solution(m, n, board):
    answer = 0

    board=rotate(board)

    while True:
        board,cnt=remove_block(board,n,m)

        if cnt>0:
            answer+=cnt
        else:
            break
    return answer