from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    len_weak=len(weak)
    dist_comb=list(map(list,permutations(dist,len(dist))))

    for i in range(len(weak)):
        weak.append(weak[i]+n)
    
    for start in range(len_weak):
        friends = weak[start:start+len_weak]
        for d in dist_comb:
            cnt=1
            distance=0
            check_dist=friends[0]+d[0]
            for i in range(len_weak):
                if friends[i]>check_dist:
                    cnt+=1
                    if cnt>len(d):
                        break
                    distance+=1
                    check_dist=friends[i]+d[distance]
            answer = min(answer,cnt)
    if answer>len(dist):
        answer=-1
            
    return answer