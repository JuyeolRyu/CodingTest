#https://programmers.co.kr/learn/courses/30/lessons/72410
import re
def solution(new_id):
    answer = ''
    print(new_id)
    #1단계
    new_id = new_id.lower()
    print(new_id)
    #2단계
    new_id = re.sub('[\a-z\b\-\_\.]','',new_id)
    print(new_id)
    #3단계
    new_id = re.sub('\.+','.',new_id)
    print(new_id)
    #4단계
    if new_id and new_id[0] == '.':
        new_id = new_id[1:]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    #5단계
    if not new_id:
        new_id = 'a'
    print(new_id)
    #6단계
    if len(new_id) > 15:
        new_id = new_id[:16]
    if new_id and new_id[-1] == '.':
        new_id = new_id[:-1]
    print(new_id)
    return answer