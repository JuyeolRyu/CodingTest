import heapq
def solution(operations):
    answer = []
    maxQ = []
    minQ = []
    for o in operations:
        oper,num = o.split()
        if oper == 'I':
            heapq.heappush(minQ,int(num))
            heapq.heappush(maxQ,-int(num))
        elif maxQ or minQ:
            if int(num) == 1:
                heapq.heappop(maxQ)
                minQ=[]
                for n in maxQ:
                    heapq.heappush(minQ,-n)
            else:
                heapq.heappop(minQ)
                maxQ=[]
                for n in minQ:
                    heapq.heappush(maxQ,-n)

    if len(minQ) == 0 or len(maxQ) == 0:
        answer=[0,0]
    else:
        answer=[-heapq.heappop(maxQ),heapq.heappop(minQ)]
    return answer