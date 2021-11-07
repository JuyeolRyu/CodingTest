from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for permu in permutations(dungeons,len(dungeons)):
        tmp=0
        s=k
        for n,minus in permu:
            if s>=n:
                s-=minus
                tmp+=1
            else:
                break
        answer=max(answer,tmp)
    return answer