def solution(n):
    answer = []
    triangle = [[0]*i for i in range(1,n+1)]
    r,c,num = -1,0,1
    
    for i in range(n):
        for j in range(i,n):
            if i%3 == 0:
                r+=1
            elif i%3 == 1:
                c+=1
            else:
                r-=1
                c-=1
            triangle[r][c]=num
            num+=1

    answer = sum(triangle,[])
    return answer