'''
[팰린드롬]
문자열을 입력받아 좌우 대칭이 되도록 배치한다.(여러개일 경우 사전순으로 앞서는 것을 선택)
'''
from collections import defaultdict
ans = ''
odd_ans = ''
dic = defaultdict(int)
odd = 0
for c in input().rstrip():
  dic[c]+= 1
dic = dict(sorted(dic.items(),key = lambda x:x[0]))
for c in dic:
  if dic[c]%2 != 0:
    odd+=1
    odd_ans += c
  ans+=(c*(dic[c]//2))
if odd>1:
  print("I'm Sorry Hansoo")
else:
  print(ans+odd_ans+"".join(list(reversed(ans))))