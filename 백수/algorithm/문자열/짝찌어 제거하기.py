#https://programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    stack = []
    for c in s:
        if stack and stack[-1] == c:
            stack.pop(-1)
            continue
        stack.append(c)
    if not stack:
        return 1
    else:
        return 0