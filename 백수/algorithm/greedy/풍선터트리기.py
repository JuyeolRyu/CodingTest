def solution(A):
    answer = 2
    left_min,right_min = A[0],A[-1]
    left,right = 1,len(A)-2
    while left<=right:
        if left_min<right_min:
            if A[right]<right_min:
                right_min=A[right]
                answer+=1    
            right-=1
        else:
            if A[left]<left_min:
                left_min=A[left]
                answer+=1
            left+=1

    return answer