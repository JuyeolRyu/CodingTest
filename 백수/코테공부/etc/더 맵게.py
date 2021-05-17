import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if len(scoville) >= 2:
            a = heapq.heappop(scoville)
            if a>=K:
                break
            b = heapq.heappop(scoville)
            heapq.heappush(scoville,a+(b*2))
            answer += 1
        else:
            a = heapq.heappop(scoville)
            if a<K:
                return -1

    return answer