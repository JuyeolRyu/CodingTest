#https://programmers.co.kr/learn/courses/30/lessons/42587
#프린터 (스택/큐)
def solution(p, location):
    ans = 0
    while len(p) > 0:
        max_num = max(p)
        l = len(p)
        num = p.pop(0)
        if num == max_num:
            ans += 1
            if location == 0:
                break
            location -= 1
            continue
        
        location = (location+l-1)%l
        p.append(num)

    return ans