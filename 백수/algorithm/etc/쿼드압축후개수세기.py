answer = [0,0]
def bin_search(arr,s,e):
    if s==e:
        if arr[s[0]][s[1]] == 0:
            answer[0]+=1
        else:
            answer[1]+=1
        return
    row_mid = (s[0]+e[0])//2
    col_mid = (s[1]+e[1])//2
    cnt=0
    for row in range(s[0],e[0]+1):
        cnt+=arr[row][s[1]:e[1]+1].count(1)

    if cnt == 0:
        answer[0]+=1
        return
    elif cnt == (e[0]-s[0]+1)**2:
        answer[1]+=1
        return
    elif cnt != (e[0]-s[0]+1)**2:
        bin_search(arr,[s[0],s[1]],[row_mid,col_mid])
        bin_search(arr,[s[0],col_mid+1],[row_mid,e[1]])
        bin_search(arr,[row_mid+1,s[1]],[e[0],col_mid])
        bin_search(arr,[row_mid+1,col_mid+1],[e[0],e[1]])
    return
def solution(arr):
    start,end=[0,0],[len(arr)-1,len(arr)-1]
    bin_search(arr,start,end)

    return answer