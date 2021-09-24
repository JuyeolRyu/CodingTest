def is_valid(s):
    stack = [s[0]]
    for c in s[1:]:
        if stack and ((stack[-1]=='[' and c==']') or (stack[-1]=='{' and c=='}') or (stack[-1]=='(' and c==')')):
            stack.pop()
        else:
            stack.append(c)
            
    if stack:
        return False
    return True
            
def solution(s):
    answer = 0
    for i in range(len(s)):
        if is_valid(s[i:]+s[:i]):
            answer+=1
    return answer