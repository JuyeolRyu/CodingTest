n,m = map(int,input().split())
lst = list(map(int,input().split()))
start = 0
end = max(lst)

#
while start <= end:
    #자른 빵 길이의 합
    tmp_sum = 0
    #자를 위치
    mid = (start+end) //2

    for num in lst:
        #빵을 자를 수 있으면 길이 추가
        if num > mid:
            tmp_sum += (num-mid)
    
    #자른 빵 길이의 합이 기준치보다 작은 경우
    if tmp_sum < m:
        #끝 범위를 mid - 1
        end = mid - 1
    #더 잘라도 되는 경우
    else:
        ans = mid
        start = mid + 1

print(ans)