import math
def solution(n,a,b):
    answer = 0
    t = 1
    if a>b:
        a,b = b,a
    while True:
        if a%2 != 0 and a+1 == b:
            answer = t
            break

        a =math.ceil(a/2)
        b =math.ceil(b/2)
        t+=1

    return answer