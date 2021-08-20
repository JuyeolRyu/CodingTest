import heapq
def get_task(q,jobs,time):
    while jobs and jobs[0][0] <= time:
        tmp = jobs.pop(0)
        heapq.heappush(q,[tmp[1],tmp[0]])
def solution(jobs):
    answer = 0
    
    n = len(jobs)
    jobs = sorted(jobs,key=lambda x:(x[0],x[1]))
    time = jobs[0][0]
    q=[]
    get_task(q,jobs,time)

    while jobs or q:
        need,start = heapq.heappop(q)
        time += need
        answer += (time-start)
        
        get_task(q,jobs,time)
            
        if not q and jobs:
            time=jobs[0][0]
            get_task(q,jobs,time)
            
    return answer//n 