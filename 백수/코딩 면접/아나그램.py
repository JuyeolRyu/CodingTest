'''
Anagram
두개의 문자열을 각각 재배열 했을때 같은 단어 혹은 문자열이 있으면 아나그램이다.
아나그램이면 True 아니면 False를 출력해라.
'''
str1 = 'apple pie'
str2 = 'ppap liee'
str1 = sorted(str1.lower())
str2 = sorted(str2.lower())
if str1 == str2:
  print(True)
else:
  print(False)