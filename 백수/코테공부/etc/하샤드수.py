def solution(x):
    n = sum(list(map(int,str(x))))
    if x%n == 0:
        return True
    else:
        return False