#https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    ans = [True]*(n+1)
    lost.sort()
    reserve.sort()
    for l in lost:
        if l in reserve:
            reserve.remove(l)
        else:
            ans[l] = False
    for l in lost:
        if not ans[l]:
            if l-1 in reserve:
                reserve.remove(l-1)
                ans[l] = True
            elif l+1 in reserve:
                reserve.remove(l+1)
                ans[l] = True
    
    return ans.count(True)-1