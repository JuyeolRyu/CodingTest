def solution(number, k):
    stack = []
    for idx,n in enumerate(number):
        if not stack or int(stack[-1]) > int(n):
            stack.append(n)
        else:
            while int(stack[-1]) < int(n):
                stack.pop()
                k -= 1
                
                if k == 0:
                    return "".join(stack)+"".join(number[idx:])
                
                if not stack:
                    break
            stack.append(n)
    return "".join(stack[:-k])


'''
from itertools import combinations
def solution(number, k):
    answer = 0
    number=list(number)
    for i in combinations(number,len(number)-k):
        answer = max(answer,int("".join(i)))
    
    return str(answer)
'''