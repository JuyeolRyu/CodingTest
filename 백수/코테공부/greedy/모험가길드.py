ans = 0
max_fear = 0
people_num = 0

#입력
n = int(input())
fears = list(map(int,input().split()))
#공포도 정렬
fears = sorted(fears)

for fear in fears:
  #그룹에 포함된 사람 수 증가
  people_num += 1
  #현재 그룹중 가장 큰 공포도 정하기
  max_fear = max(fear,max_fear)
  #그룹 내 사람수가 공포도보다 크거나 같아지면 그룹 결성
  if(people_num >= max_fear):
    people_num = 0
    max_fear = 0
    ans += 1

print(ans)