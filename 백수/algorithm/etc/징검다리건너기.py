#이진탐색
def solution(stones, k):
    answer = 0
    left,right=0,max(stones)
    while left<=right:
        cnt = 0
        is_possible = True
        mid = (left+right)//2
        for stone in stones:
            if mid>stone:
                cnt+=1
                if cnt>=k:
                    is_possible=False
                    break
            else:
                cnt=0
        if is_possible:
            answer = max(answer,mid)
            left=mid+1
        else:
            right=mid-1
    return answer

#완전탐색-시간초과
def solution(stones, k):
    answer = float('inf')
    for i in range(len(stones)-k):
        answer = min(answer,max(stones[i:i+k]))
    return answer
