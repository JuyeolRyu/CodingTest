#https://programmers.co.kr/learn/courses/30/lessons/12915
def solution(strings, n):
    strings = sorted(strings, key=lambda x:(x[n],x))
    return strings