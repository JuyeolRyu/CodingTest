from itertools import combinations
def solution(nums):
    answer = 0
    for num in combinations(nums,3):
        tmp = sum(num)
        check = True
        for n in range(2,tmp):
            if tmp % n == 0:
                check = False
                break
        if check:
            answer+=1

    return answer