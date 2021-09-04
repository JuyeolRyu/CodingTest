from itertools import combinations
from collections import defaultdict
import copy
def solution(relation):
    ans = []
    li=[]
    tmp = [i for i in range(len(relation[0]))]
    for n in range(1,len(relation)):
        li.extend(map(list,combinations(tmp,n)))
    
    li2=[]
    for my_set in li:
        tmp = set()
        for r in relation:
            s = ''
            for c in my_set:
                s+=r[c]
            tmp.add(s)
        if len(tmp) == len(relation):
            li2.append(my_set)

    ans = copy.deepcopy(li2)
    for i in range(len(li2)):
        for j in range(i+1,len(li2)):
            if len(li2[i]) == len(set(li2[i])&set(li2[j])) and li2[j] in ans:
                ans.pop(ans.index(li2[j]))

    return len(ans)