#https://programmers.co.kr/learn/courses/30/lessons/43164

#sol1
import heapq
from queue import PriorityQueue

def solution(tickets):
    answer = []
    dic = {}
    visited = {}
    for t in tickets:
        if t[0] in dic:
            dic[t[0]].append(t[1])
        else:
            dic[t[0]] = [t[1]]
            
        if t[1] in visited:
            visited[t[1]] += 1
        else:
            visited[t[1]] = 1

    for d in dic:
        dic[d].sort()
    def dfs(dic,city):
        answer.append(city)
        if len(answer) == len(tickets)+1:
            return True
        if city not in dic:
            return False

        for c in dic[city]:
            if c in visited and visited[c] <= 0:
                continue
                
            visited[c] -= 1
            if dfs(dic,c):
                return True
            else:
                answer.pop(-1)
                visited[c] += 1
    dfs(dic,'ICN')

    return answer
#sol2
from collections import defaultdict

def solution(tickets):
    answer = []
    dic = defaultdict(list)
    for t in tickets:
        dic[t[0]].append(t[1])

    for d in dic:
        dic[d].sort(reverse = True)
    q = ['ICN']
    while q:
        tmp = q[-1]
        if dic[tmp]:
            q.append(dic[tmp].pop())
        else:
            answer.append(q.pop())
    answer.reverse()
    return answer