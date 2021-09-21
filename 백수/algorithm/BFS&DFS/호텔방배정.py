#sol1
from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
def dfs(cur,rooms):
    if not rooms[cur]:
        rooms[cur] = cur+1
        return cur
        
    ret = dfs(rooms[cur],rooms)
    rooms[cur] = ret+1
    return ret
    
def solution(k, rooms):
    answer = []
    room = defaultdict(int)
    for number in rooms:
        answer.append(dfs(number,room))
    return answer

#sol2 linkedList
from collections import defaultdict
def solution(k, rooms):
    answer = []
    if k==1:
        return [1]
    linked = defaultdict(list)
    linked[1] = [True,-1,2]
    linked[k] = [True,k-1,-1]
    for i in range(2,k):
        linked[i] = [True,i-1,i+1]

    for r in rooms:
        if not linked[r][0]:
            while linked[r] and not linked[r][0]:
                r = linked[r][2]
                
        linked[r][0]=False
        answer.append(r)
        prev,ne=linked[r][1],linked[r][2]
        if prev == -1 and ne == -1:
            continue
        elif prev == -1:
            linked[ne][1]=prev
        elif ne == -1:
            linked[prev][2]=ne
        else:
            linked[prev][2],linked[ne][1]=ne,prev

    return answer