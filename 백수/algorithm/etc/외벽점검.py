from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist)+1
    len_weak=len(weak)
    #1.dist의 가능한 모든 순열 저장
    dist_comb=list(map(list,permutations(dist,len(dist))))
	
    #2.weak리스트 2배로 늘려주기
    for i in range(len(weak)):
        weak.append(weak[i]+n)
    #3.weak리스트에서 시작점을 정하기 위한 반복문
    for start in range(len_weak):
    	#4.start기준으로 weak길이만큼 리스트 생성
        weak_points = weak[start:start+len_weak]
        #5.친구 순열(dist_comb)를 탐색하면서 수리 가능한 경우 찾기
        for d in dist_comb:
            #6.사용한 친구수,현재 위치
            cnt=1
            cur_position=friends[0]+d[0]
            for weak_point in weak_points[1:]:
            	#7.현재 위치보다 결함지점이 뒤에 있는 경우
                if weak_point>cur_position:
                    #8-1.정해진 친구 범위 벗어난 경우 탈출
                    if cnt+1>len(d):
                        cnt+=1
                        break
                    #8-2.현재 위치 갱신
                    cur_position=friend+d[cnt]
                    cnt+=1
            #9.가장 작은 값으로 answer 갱신
            answer = min(answer,cnt)
    if answer>len(dist):
        answer=-1
            
    return answer