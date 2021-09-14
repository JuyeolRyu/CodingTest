def solution(enter, leave):
    answer = [0]*(len(enter)+1)
    q=[enter[0]]
    enter_idx=1
    while q:
        while q and leave[0] in q:
            q.pop(q.index(leave[0]))
            answer[leave[0]] += len(q)
            leave = leave[1:]
            for n in q:
                answer[n]+=1
        if enter_idx < len(enter):
            q.append(enter[enter_idx])
            enter_idx+=1
    return answer[1:]