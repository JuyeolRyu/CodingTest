import heapq
def timeToSecond(s):
    return sum(list(map(lambda x:int(x[1])*(60**(2-x[0])),enumerate(s.split(":")))))
def secondToTime(n):
    h="0"+str(n//3600)
    m="0"+str((n%3600)//60)
    s="0"+str(n%3600%60)
    return h[-2:]+":"+m[-2:]+":"+s[-2:]
def solution(play_time, adv_time, logs):
    answer = [0,0]
    play_time = timeToSecond(play_time)
    adv_time = timeToSecond(adv_time)
    time_table=[0]*(play_time+1)
    for i,log in enumerate(logs):
        start,end = logs[i].split("-")
        logs[i] = [timeToSecond(start),timeToSecond(end)]
        time_table[logs[i][0]]+=1
        time_table[logs[i][1]]-=1
            
    for t in range(1,play_time+1):
        time_table[t] += time_table[t-1]
    for t in range(1,play_time+1):
        time_table[t] += time_table[t-1]
    
    answer = [time_table[adv_time-1],0]
    for t in range(adv_time,play_time):
        if answer[0] < (time_table[t]-time_table[t-adv_time]):
            answer = [time_table[t]-time_table[t-adv_time], t+1-adv_time]

    return secondToTime(answer[1])