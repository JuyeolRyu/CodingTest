#https://ktko.tistory.com/entry/%EC%9E%90%EB%B0%94-%EC%86%90%EC%BD%94%EB%94%A9-%EB%AC%B8%EC%A0%9C
# 버블
a=[6,5,8,1,9,3]
for i in range(len(a)-1):
  for j in range(len(a)-i-1):
    if a[j] > a[j+1]:
      a[j],a[j+1] = a[j+1],a[j]
print(a)
#선택
a=[6,5,8,1,9,3]
for i in range(len(a)):
  min_num = [float('inf'),0]
  for j in range(i,len(a)):
    if a[j] < min_num[0]:
      min_num[0] = a[j]
      min_num[1] = j
  a[i],a[min_num[1]] = a[min_num[1]],a[i]
print(a)
#삽입
a=[6,5,8,1,9,3]
for i in range(1,len(a)):
  for j in range(i,0,-1):
    if a[j]<a[j-1]:
      a[j],a[j-1] = a[j-1],a[j]
    else:
      break
print(a)
#힙
def heapify(li, idx, n):
  print(idx,li)
  l = idx * 2;
  r = idx * 2 + 1
  s_idx = idx
  if (l <= n and li[s_idx] > li[l]):
      s_idx = l
  if (r <= n and li[s_idx] > li[r]):
      s_idx = r
  if s_idx != idx:
      li[idx], li[s_idx] = li[s_idx], li[idx]
      return heapify(li, s_idx, n)

v = [6,3,8,9,2,3]
n = len(v)
v = [0]+v

# min heap 생성
for i in range(n, 0, -1) :
    heapify(v, i, n)
print(v)
#퀵

#머지