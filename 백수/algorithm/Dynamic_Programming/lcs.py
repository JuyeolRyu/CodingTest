#https://www.acmicpc.net/problem/9251
#lcs 최장 중복 수열 찾는 문제
s1 = input()
s2 = input()
lcs = [[0 for i in range(len(s2)+1)] for j in range(len(s1)+1)]

for r in range(len(s1)):
  for c in range(len(s2)):
    if s1[r] == s2[c]:
      lcs[r+1][c+1] = lcs[r][c]+1
    else:
      lcs[r+1][c+1] = max(lcs[r][c+1],lcs[r+1][c])

print(lcs[-1][-1])