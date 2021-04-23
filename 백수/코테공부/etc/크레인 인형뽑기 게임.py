#https://programmers.co.kr/learn/courses/30/lessons/64061?language=python3
def solution(board, moves):
    answer = 0
    stack = [-1]
    
    for m in moves:
        for b in board:
            if b[m-1] != 0:
                stack.append(b[m-1])
                b[m-1] = 0
                if stack[-1] == stack[-2]:
                    stack.pop(-1)
                    stack.pop(-1)
                    answer+=2
                break

    return answer



'''
[0, 0, 0, 0, 0]
[0, 0, 1, 0, 3]
[0, 2, 5, 0, 1]
[4, 2, 4, 4, 2]
[3, 5, 1, 3, 1]
'''