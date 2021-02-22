#https://www.acmicpc.net/problem/1700
n,k = map(int,input().split())
arr = list(map(int,input().split()))
q = []
tmp_q = []

ans = 0

for idx,num in enumerate(arr):
  #이미 큐에 값이 들어있으면 인덱스만 초기화
  if num in q:
    for i,val in enumerate(tmp_q):
      if val[0] == num:
        if num not in arr[idx+1:]:
          tmp_q[i][1] = 100
        else:
          tmp_q[i][1] = arr[idx+1:].index(num)+idx+1
  #아직 큐가 다 안채워졌을 경우
  elif len(q) < n:
    q.append(num)
    if num not in arr[idx+1:]:
      tmp_q.append([num,100])
    else:
      i = arr[idx+1:].index(num)
      tmp_q.append([num,i+idx+1])
  #큐가 다 차있고 새로운 값이 들어가야 할때
  else:
    tmp_q = sorted(tmp_q,key=lambda x:x[1],reverse=True)
    val = tmp_q.pop(0)
    q.pop(q.index(val[0]))
    q.append(num)
    if num not in arr[idx+1:]:
      tmp_q.append([num,100])
    else:
      i = arr[idx+1:].index(num)
      tmp_q.append([num,i+idx+1])
    ans +=1

print(ans)