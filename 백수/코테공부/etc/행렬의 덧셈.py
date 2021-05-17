def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        tmp = []
        for j in range(len(arr1[i])):
            tmp.append(arr1[i][j]+arr2[i][j])
        answer.append(tmp)
    return answer