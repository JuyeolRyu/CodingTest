#https://www.acmicpc.net/problem/17609
n = int(input())
strings = [input() for i in range(n)]

def search(s,left,right,check):
  while left < right:
    if s[left] == s[right]:
      left += 1
      right -= 1
      continue
    else:
      if check:
        return 2
      else:
        ans = float('inf')
        if left+1 == right:
          return 1
        if s[left+1] == s[right]:
          ans = min(search(s,left+1,right,True), ans)
        if s[left] == s[right-1]:
          ans = min(search(s,left,right-1,True), ans)
        if s[left+1] != s[right] and s[left] != s[right-1]:
          return 2
        return ans

  if check:
    return 1
  return 0

for s in strings:
  left = 0
  right = len(s)-1
  print(search(s,left,right,False))

'''
1
baaba

5
aaa
aab
baa
aaba
aabaa

1
aapqbcbqpqaa
'''