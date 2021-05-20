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

#힙

#퀵

#머지