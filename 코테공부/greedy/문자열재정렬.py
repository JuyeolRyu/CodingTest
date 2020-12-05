s = input()
string = ''
num = 0

for c in s:
  if c.isdigit():
    num += int(c)
  else:
    string += c

string = ''.join(sorted(string))
print(string + str(num))

#list = str.split()  ==> 문자열을 리스트로 바꾸기
#” “.join( list )    ==> 리스트를 문자열로 바꾸기