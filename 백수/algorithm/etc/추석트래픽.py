import math
def solution(lines):
    answer = 0
    time_list = []
    for line in lines:
        t,t_diff = line.split(' ')[1:]
        h,m,s = t.split(':')
        time_list.append([int((3600*float(h)+60*float(m)+float(s)-float(t_diff[:-1]))*1000)+1, int((60*60*float(h)+60*float(m)+float(s))*1000) ])
    
    print(time_list)
    for t in time_list:
        s,e = t[0],t[0]+1000
        s1,e1 = t[1],t[1]+1000
        cnt,cnt2 = 0,0
        for t2 in time_list:
            s2,e2 = t2
            if s<=e2 and s2<e:
                cnt += 1
            
            if s1<=e2 and s2<e1:
                cnt2 += 1
        answer = max(answer,cnt,cnt2)
    return answer