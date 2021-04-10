#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    book = {}
    for p in phone_book:
        book[p] = 1
        
    for b in book:
        tmp = ''
        for n in b:
            tmp += n
            if tmp in book and tmp != b:
                return False

    return True