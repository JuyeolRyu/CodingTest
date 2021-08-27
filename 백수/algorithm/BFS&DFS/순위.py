#https://programmers.co.kr/learn/courses/30/lessons/49191
from collections import defaultdict
def solution(n, results):
    def dfs(start,reverse):
        ret = 0
        my_path = reverse_path if reverse else path
        for ne_node in my_path[start]:
            if ne_node not in visited:
                visited.add(ne_node)
                ret += dfs(ne_node,reverse)
                
        return ret+1
    answer = 0
    
    path = defaultdict(list)
    reverse_path = defaultdict(list)
    
    for win,lose in results:
        path[win].append(lose)
        reverse_path[lose].append(win)
    
    for node in range(1,n+1):
        cnt = 0
        if node in path:
            visited = set({node})
            cnt += dfs(node,False)-1
        if node in reverse_path:
            visited = set({node})
            cnt += dfs(node,True)-1
            
        if cnt == n-1:
            answer+=1

    return answer