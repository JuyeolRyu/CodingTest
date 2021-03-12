#try 1
def solution(gems):
    end = 0
    start = 0
    gem_set = list(set(gems))
    dic = dict()
    ans = []
    #시작 부터 탐색시작
    tmp_set = gem_set[:]
    for idx,gem in enumerate(gems[start:]):
        if gem in tmp_set:
            tmp_set.pop(tmp_set.index(gem))
        if len(tmp_set) == 0:
            end = idx
            break
    while True:
        if end == len(gems):
            break
        
        check = False 
        tmp_set2 = gem_set[:]
        
        for idx in range(end,-1,-1):
            if gems[idx] in tmp_set2:
                tmp_set2.pop(tmp_set2.index(gems[idx]))
            if len(tmp_set2) == 0:
                start = idx
                check = True
                break
        if check:
            dic[end] = [start+1,end+1]
        end += 1
        
    min_num = float('inf')
    for idx in dic:
        if dic[idx][1] - dic[idx][0] < min_num:
            ans = [dic[idx][0],dic[idx][1]]
            min_num = dic[idx][1] - dic[idx][0]
    return ans

#try2
def solution(gems): 
    size = len(set(gems)) 
    dic = {gems[0]:1} 
    temp = [0, len(gems) - 1] 
    #답이 될 수 있는 후보 
    start , end = 0, 0 
    while(start < len(gems) and end < len(gems)): 
        if len(dic) == size: 
            if end - start < temp[1] - temp[0]: 
                temp = [start, end] 
            if dic[gems[start]] == 1: 
                del dic[gems[start]] 
            else: dic[gems[start]] -= 1 
            start += 1 
        else: 
            end += 1 
            if end == len(gems): 
                break 
            if gems[end] in dic.keys(): 
                dic[gems[end]] += 1 
            else: dic[gems[end]] = 1 
    return [temp[0]+1, temp[1]+1]