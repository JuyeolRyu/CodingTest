#https://programmers.co.kr/learn/courses/30/lessons/12925
def solution(s):
    if s[0].isdigit():
        return int(s)
    else:
        if s[0] == '-':
            return -int(s[1:])
        return int(s[1:])