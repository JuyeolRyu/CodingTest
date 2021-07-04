#https://www.acmicpc.net/problem/9252

s1 = input()
s2 = input()
c = len(s1)
r = len(s2)
dp = [[0 for i in range(c+1)] for j in range(r+1)]

for i2 in range(r):
  for i1 in range(c):
    if s2[i2] == s1[i1]:
      dp[i2+1][i1+1] = dp[i2][i1]+1
    else:
      dp[i2+1][i1+1] = max(dp[i2][i1+1],dp[i2+1][i1])

def sol():
  ans = ''
  val = dp[-1][-1]
  r = len(dp)-1
  c = len(dp[0])-1
  while val != 0:
    if val-1 == dp[r-1][c] and val-1 == dp[r][c-1]:
      val -= 1
      ans = s1[c-1]+ans
      r -= 1
      c -= 1
    else:
      if dp[r-1][c] > dp[r][c-1]:
        r -= 1
      else:
        c -= 1  
  return ans

print(dp[-1][-1])
print(sol())

'''
ADQWEQWDQWGFSDAHWREYERFGD
FGDGFDSGWERDSAFLSD

ASDWADGFRQWE
GHASDQWEZZZZZ

a
aaaaaaaaaaaaaaaa

CCCBBBACA
AAACCCABA

ZAZAZA
AZAZA
'''