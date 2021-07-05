#후위 표기식
#https://www.acmicpc.net/problem/1918

#sol1
import sys
input = sys.stdin.readline
s = input().rstrip()
prec = {'*':2,'/':2,'+':1,'-':1,'(':0}
stack = []
ans = ""
for c in s:
    if c.isalpha():
        ans = ans+c
    elif c == ')':
        while True:
            tmp_c = stack.pop(-1)
            if tmp_c == '(':
                break
            else:
                ans = ans+tmp_c
    elif c == '(':
        stack.append(c)
    else:
        while stack and prec[c] <= prec[stack[-1]]:
            ans += stack.pop(-1)
        stack.append(c)

while stack:
    ans += stack.pop(-1)
print(ans)