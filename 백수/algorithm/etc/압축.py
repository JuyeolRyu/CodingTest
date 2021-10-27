from collections import defaultdict
def solution(msg):
    answer = []
    dic=defaultdict(int)
    n,idx=1,0
    for i in range(65,91):
        dic[chr(i)]=n
        n+=1
    
    s=msg[idx]
    while idx<len(msg):
        while True:
            if s not in dic:
                dic[s]=n
                n+=1
                break
            
            idx+=1
            if idx>=len(msg):
                s+=" "
                break
            s+=msg[idx]
        
        answer.append(dic[s[:-1]])
        s=s[-1]

    return answer