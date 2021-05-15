from itertools import combinations
def solution(numbers):
    answer = []
    for n in combinations(numbers,2):
        answer.append(n[0]+n[1])
    answer = sorted(list(set(answer)))
    return answer