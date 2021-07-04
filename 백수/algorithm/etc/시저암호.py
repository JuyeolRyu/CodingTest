def solution(s, n):
    answer = ''
    for c in s:
        if c.isalpha():
            num = ord(c)
            if num >= 97:
                answer += chr((num-97+n)%26+97)
            else:
                answer += chr((num-65+n)%26+65)
        else:
            answer += ' '

    return answer