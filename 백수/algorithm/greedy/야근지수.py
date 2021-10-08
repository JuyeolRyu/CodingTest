import heapq

def solution(n, works):
    zero_cnt = 0
    works = list(map(lambda x:-x,works))
    heapq.heapify(works)
    while n>0:
        if zero_cnt == len(works):
            break
        num = -heapq.heappop(works)
        diff = num+works[0]
        ne_num = 0
        if n>=diff:
            if diff==0:
                diff=1
            n-=diff
            ne_num = -(num-diff)
        else:
            ne_num = -(num-n)
            n=0
            
        if ne_num == 0:
            zero_cnt+=1
        heapq.heappush(works,ne_num)
    return sum(list(map(lambda x:x**2,works)))