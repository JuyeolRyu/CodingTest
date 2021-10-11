import re
def hashtagToAlpha(m):
    m=re.sub('C#','c',m)
    m=re.sub('D#','d',m)
    m=re.sub('E#','e',m)
    m=re.sub('F#','f',m)
    m=re.sub('G#','g',m)
    m=re.sub('A#','a',m)
    m=re.sub('B#','b',m)
    return m
def timeToMinute(t):
    H,M=map(int,t.split(":"))
    return 60*H+M
def solution(m, musicinfos):
    answer = [float('inf'),0,'(None)']#music,start,len
    m=hashtagToAlpha(m)
    
    for music in musicinfos:
        info=music.split(',')
        info[0]=timeToMinute(info[0])
        info[1]=timeToMinute(info[1])
        info[3]=hashtagToAlpha(info[3])
        if info[1]-info[0]>=len(info[3]):
            info[3] = info[3]*((info[1]-info[0])//len(info[3]))+info[3][:(info[1]-info[0])%len(info[3])]
        else:
            info[3] = info[3][:(info[1]-info[0])%len(info[3])]
        s=re.findall(m,info[3])
        if s:
            if answer[1]<info[1]-info[0]:
                answer=[info[0],info[1]-info[0],info[2]]
            elif answer[1]==info[1]-info[0] and info[0]<answer[0]:
                answer=[info[0],info[1]-info[0],info[2]]
        #print(info)
    return answer[2]