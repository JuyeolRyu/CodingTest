from collections import defaultdict
def solution(table, languages, preference):
    answer = []
    dic=defaultdict(list)
    for t in table:
        t=t.split()
        dic[t[0]]=t[1:]
        answer.append([0,t[0]])

    for idx,key in enumerate(answer):
        n,key = key
        for i,language in enumerate(languages):
            if language in dic[key]:
                answer[idx][0]+=preference[i]*(5-dic[key].index(language))
                
    answer = sorted(answer,key=lambda x:(-x[0],x[1]))
    return answer[0][1]