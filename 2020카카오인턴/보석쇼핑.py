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
