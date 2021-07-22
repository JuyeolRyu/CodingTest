#IPv6
#https://www.acmicpc.net/problem/3107

#sol1(문자열)
import sys
input = sys.stdin.readline

s = input().rstrip()

colon_idx = s.find("::")
colon_num = s.count(":")

if colon_idx >= 0:
    if colon_num > 7:
        s = s[:colon_idx]+(7-colon_num)*":"+s[colon_idx+1:]
        colon_num-=1
    else:
        s = s[:colon_idx]+(7-colon_num)*":"+s[colon_idx:]

address = s.split(":")
for i,a in enumerate(address):
    address[i] = (4-len(a))*'0'+address[i]

print(":".join(address))

'''
::1:1:1:1:1:1
1:2:3:4:5:6:7::
'''