from collections import defaultdict
def dfs(tree,query):
    ret = 0
    if len(query) == 1:
        query = int(query[0])
        for n in tree:
            if n>=query:
                ret += 1
        return ret
    
    node = query.pop(0)
    if node != '-' and node not in tree:
        return 0
    if node == '-':
        for ne_node in tree:
            ret += dfs(tree[ne_node],query[:])
    else:
        ret += dfs(tree[node],query)
    return ret
def solution(info, query):
    answer = []
    root = {}
    dic = root
    for i in info:
        i = i.split(" ")
        for s in i[:-2]:
            if s not in dic:
                dic[s] = {}
            dic = dic[s]

        if i[-2] not in dic:
            dic[i[-2]] = [int(i[-1])]
        else:
            dic[i[-2]].append(int(i[-1]))
        dic = root
    
    for q in query:
        q = q.split(" and ")
        tmp = q.pop()
        q = q+tmp.split(" ")
        answer.append(dfs(root,q))
    return answer