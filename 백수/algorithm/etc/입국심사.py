#sol1 시간초과(heapq)
import heapq
def solution(n, times):
    answer = 0
    q = []
    for t in times:
        heapq.heappush(q,[t,t])
        
    while n>0:
        tmp = heapq.heappop(q)
        heapq.heappush(q,[tmp[0]+tmp[1],tmp[1]])
        n-=1

        answer = tmp[0]

    return answer

#sol2 시간초과(정렬)
def solution(n, times):
    q = []
    for t in times:
        for i in range(1,n+1):
            q.append(t*i)
    q.sort()

    return q[n-1]

#sol3 이분탐색-파이썬
def solution(n, times):
    ans = float('inf')
    max_time = max(times)*n
    min_time = 0
    
    while min_time < max_time-1:
        total = 0
        mid = (min_time+max_time)//2

        for t in times:
            total += mid//t

        if total >= n:
            max_time = mid
            ans = min(ans,mid)
        elif total < n:
            min_time = mid
            
    return answer
#sol4 이분탐색-자바스크립트
function solution(n, times) {
    var answer = Infinity;
    var min_time = 0;
    var max_time = Math.max(...times)*n;
    

    while(min_time<max_time-1){
        var total_sum = 0;
        var mid = Math.floor((min_time+max_time)/2);
        
        times.map((t)=>{
            total_sum += Math.floor(mid/t)
        })
        if(total_sum >= n){
            max_time = mid;
            answer = Math.min(answer,mid);
        }else{
            min_time = mid;
        }
    }
    return answer;
}