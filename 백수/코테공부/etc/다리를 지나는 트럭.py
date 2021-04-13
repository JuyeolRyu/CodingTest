#https://programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque
def solution(b_len, w, tw):
    T = 1
    q = deque()
    out_time = deque()
    q.append(tw.pop(0))
    out_time.append(T+b_len-1)

    while q:
        if out_time[0] == T:
            out_time.popleft()
            q.popleft()
        if len(tw) > 0 and tw[0] + sum(q) <= w:
            q.append(tw.pop(0))
            out_time.append(T+b_len)

        T+=1

    return T