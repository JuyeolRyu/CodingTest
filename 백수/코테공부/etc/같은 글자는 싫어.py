def solution(arr):
    answer = []
    prev = arr[0]
    for num in arr[1:]:
        if num == prev:
            continue
        else:
            answer.append(prev)
            prev = num
    answer.append(prev)
    return answer