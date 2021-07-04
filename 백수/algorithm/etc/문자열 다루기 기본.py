#https://programmers.co.kr/learn/courses/30/lessons/12918
def solution(s):
    def check(s):
        for c in s:
            if c.isalpha():
                return False
        return True
    
    if (len(s) ==4 or len(s)==6) and check(s):
        return True
    else:
        return False