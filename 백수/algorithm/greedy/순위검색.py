#sol1 시간초과
from collections import defaultdict
import re
def solution(info, query):
    answer = []
    score = []
    dic = defaultdict(list)
    n = len(info)
    for i,s in enumerate(info):
        s = s.split(" ")
        score.append([int(s[-1]),i])
        for idx in s[:-1]:
            dic[idx].append(i)
    dic["-"]=[i for i in range(n)]
    score.sort()
    print(score)
    for q in query:
        cnt = 0
        q=re.sub("and ","",q)
        q=q.split(" ")

        default_idx = set([i for i in range(n)])

        for s in q[:-1]:
            default_idx = default_idx&set(dic[s])

        for i in default_idx:
            if score[i][0]>=int(q[-1]):
                cnt+=1
        answer.append(cnt)
    return answer
#sol2 binary_search,hash
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
import re
def solution(info, query):
    answer = []
    dic = defaultdict(list)
    scores = []
    for i,s in enumerate(info):
        s = s.split(" ")
        scores.append(int(s[-1]))
        for n in range(1,5):
            for s_comb in combinations(s[:-1],n):
                dic["".join(list(s_comb))].append(int(s[-1]))
    dic["empty"] = scores
    for key in dic:
        dic[key].sort()
    for q in query:
        cnt = 0
        q=re.sub("and ","",q)
        q=re.sub("- ","",q)
        q=q.split(" ")
        score = int(q[-1])
        q = "".join(q[:-1])
        
        li = []
        if not q:
            li = dic["empty"]
        else:
            li = dic[q]
        
        start = bisect_left(li,score)
        if start != -1:
            answer.append(len(li)-start)
        else:
            answer.append(0)

    return answer