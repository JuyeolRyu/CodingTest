#1
def solution(absolutes, signs):
    ans = 0
    for i in range(len(absolutes)):
        if signs[i]:
            ans += absolutes[i]
        else:
            ans -= absolutes[i]
    return ans

#2
def solution(s):
    s = list(s)
    answer = 0
    def isValid():
        x,y,z =0,0,0
        for c in s:
            if (c == ']' and x == 0) or (c == ')' and y == 0) or (c == '}' and z == 0):
                return False
            if c == '[':
                x += 1
            elif c == '(':
                y+=1
            elif c == '{':
                z+=1
            elif c == ']':
                x -= 1
            elif c == ')':
                y-=1
            elif c == '}':
                z-=1
        if x == 0 and y ==0 and z ==0:
            return True
        else:
            return False
    if isValid():
        answer += 1
    for i in range(1,len(s)):
        tmp = s.pop(0)
        s.append(tmp)
        if isValid():
            answer += 1
    return answer

#3

from collections import deque

def solution(a, edges):
    if sum(a) != 0:
        return -1

    dic = {}
    for e in edges:
        if e[0] in dic:
            dic[e[0]].append(e[1])
        else:
            dic[e[0]] = [e[1]]

        if e[1] in dic:
            dic[e[1]].append(e[0])
        else:
            dic[e[1]] = [e[0]]
    q = deque()
    for d in dic:
        if len(dic[d]) == 1:
            q.append(d)

    ans = 0

    while q:
        cur = q.popleft()
        if len(dic[cur]) == 1:
            for edge in dic[cur]:
                a[edge] += a[cur]
                ans += abs(a[cur])
                q.append(edge)
                dic[edge].remove(cur)
                dic[cur].remove(edge)

    return ans
