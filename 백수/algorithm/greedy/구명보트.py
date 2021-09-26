def solution(people, limit):
    answer = 0
    l,r=0,len(people)-1
    pop_cnt = 0
    people.sort()
    while l<r:
        if people[l]+people[r]<=limit:
            l+=1
            r-=1
            pop_cnt+=2
        else:
            r-=1
            pop_cnt+=1
        answer+=1
    if len(people) != pop_cnt:
        answer+=1
    return answer