#https://www.acmicpc.net/problem/1316
n = int(input())
ans = 0
for i in range(n):
  s = input()
  char_set = set()
  prev_char = ''
  check = True
  for c in s:
    if c not in char_set:
      char_set.add(c)
    else:
      if prev_char != c:
        check = False
        break
    prev_char = c
  if check:
    ans += 1
print(ans)