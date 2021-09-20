import re
ans = set()
def find_set(case,depth,candidate):
    if depth == len(candidate):
        case.sort()
        ans.add("".join(case))
        return
    
    for bid in candidate[depth]:
        if bid not in case:
            find_set(case+[bid],depth+1,candidate)
        
def solution(user_id, banned_id):
    candidate = []
    for bid in banned_id:
        bid = re.sub('\*','.',bid)     
        p = re.compile(bid)
        tmp = []
        for uid in user_id:
            if len(bid) == len(uid) and p.match(uid):
                tmp.append(uid)
        candidate.append(tmp)
    
    find_set([],0,candidate)
    return len(ans)