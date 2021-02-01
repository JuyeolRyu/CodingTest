############################################################################################
#621. Task Scheduler                                                                       #
#https://leetcode.com/problems/task-scheduler/                                             #
############################################################################################

#sol1
import operator
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #cooldown period 가 필요하지 않은 경우
        if n == 0:
            return len(tasks)
        #각각의 문자의 개수를 세기 위해서 set 과 dict 사용한다
        ans = 0
        task_set = set(tasks)
        dic = dict()
        
        for task in task_set:
            dic[task] = tasks.count(task)
        
        #dic의 모든 items 들이 0이 될때 까지 반복
        while True:
            #가장 많이 남아있는 값이 앞으로 오도록 정렬한다
            tmp = 0
            dic = dict(sorted(dic.items(), key=operator.itemgetter(1), reverse = True))

            for task in dic:
                if dic[task] == 0:
                    continue
                else:
                    dic[task] -= 1
                    tmp += 1

                #최대 길이 도달했을 경우
                if tmp == n+1:
                    ans = ans + tmp
                    break

            #모든 값이 0이 됐는지 확인하기 위해 반복문
            check = True
            for task in dic:
                if dic[task] != 0:
                    check = False
                    break
            
            if check:
                #모든 task 완료했으나 n+1 만큼 크기가 안나왔을 경우
                if tmp != n+1:
                    ans += tmp
                break
            
            #아직 task 완료하지 못한 경우
            if tmp < n+1:
                ans += n+1
            
        return ans