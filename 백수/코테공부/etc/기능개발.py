#https://programmers.co.kr/learn/courses/30/lessons/42586
#기능개발(스택/큐)
import math
def solution(progresses, speeds):
    ans = []
    t = 0
    for i in range(len(speeds)):
        if progresses[i]+speeds[i]*t >= 100:
            ans[-1] += 1
            continue
        remain = 100-progresses[i]
        t = math.ceil(remain/speeds[i])
        ans.append(1)
    return ans