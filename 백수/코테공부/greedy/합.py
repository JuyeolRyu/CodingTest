#https://www.acmicpc.net/problem/1132
n = int(input())
dic = {}
li = []
notFirst = set()
ans = 0
for i in range(n):
  s = list(input())
  notFirst.add(s[0])
  s.reverse()
  li.append(s)
  for j in range(len(s)):
    if s[j] not in dic:
      dic[s[j]] = 10**j
    else:
      dic[s[j]] += 10**j

dic = dict(sorted(dic.items(), key = lambda x:-x[1]))

num = 9

check = False

for i in dic:
  dic[i] = num
  num -= 1
  if dic[i] == 0 and i in notFirst:
    check = True


if check:
  tmp = list(dic)
  tmp.reverse()
  for i,c in enumerate(tmp):
    if tmp[i] not in notFirst:
      break
    else:
      num = dic[tmp[i+1]]
      dic[tmp[i+1]] = dic[c]
      dic[c] = num

for s in li:
  tmp = 0
  for idx,c in enumerate(s):
    tmp += dic[c]*10**idx
  ans += tmp

print(ans)