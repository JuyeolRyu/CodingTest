#https://programmers.co.kr/learn/courses/30/lessons/12916
def solution(s):
    p = s.count('p')+s.count('P')
    y = s.count('y')+s.count('Y')
    if p == y:
        return True
    else:
        return False