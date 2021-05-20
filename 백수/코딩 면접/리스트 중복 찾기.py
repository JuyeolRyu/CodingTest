'''
다음과 같이 정렬된 리스트 3개가 주어졌을때 3개의 리스트에 모두 존재하는 값을 찾아 출력하시오.
(단, 정렬된 리스트라는 조건을 활용하여 최대한 효율적인 코드를 작성하시오)
a = [1,3,5,7,9,13,15]
b = [4,5,6,8,13]
c = [5,8,13,19]
'''
a = [1,3,5,7,9,13,15]
b = [4,5,6,8,13]
c = [5,8,13,19]

#sol1
answer = []
for i in c:
  if i in a and i in b:
    answer.append(i)
print(answer)
#sol2
answer = []
ai,bi,ci = 0,0,0
while ai<len(a) and bi<len(b) and ci<len(c):
  num = [a[ai],b[bi],c[ci]]
  min_num = min(num)

  if num[0] == num[1] == num[2]:
    ai+=1
    bi+=1
    ci+=1
    answer.append(num[0])
  elif min_num == num[0]:
    ai+=1
  elif min_num == num[1]:
    bi+=1
  elif min_num == num[2]:
    ci+=1
print(answer)