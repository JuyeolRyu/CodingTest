#https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    li = '412'
    while n>0:
        tmp = n%3
        n = n//3
        answer = li[tmp]+answer
        if tmp == 0:
            n-=1
    return answer