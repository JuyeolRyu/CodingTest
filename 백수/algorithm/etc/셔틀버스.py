def solution(n, time_diff, m, timetable):
    answer = ''
    start,end=540,540+(n-1)*(time_diff)

    idx = 0
    for i,t in enumerate(timetable):
        t = t.split(':')
        timetable[i]=int(t[0])*60+int(t[1])
    timetable.sort()
    cnt=0
    for t in range(start,end+1,time_diff):
        cnt=0
        while idx<len(timetable) and timetable[idx] <= t and cnt<m:
            cnt+=1
            idx+=1
    
    hour,minute='',''
    if cnt == m:
        hour=str((timetable[idx-1]-1)//60)
        minute=str((timetable[idx-1]-1)%60)
    elif cnt < m:
        hour=str(end//60)
        minute=str(end%60)
        
    if len(hour) == 1:
        hour='0'+hour
    if len(minute) == 1:
        minute='0'+minute
    answer=hour+':'+minute

    return answer