n = 5
m = 8
k = 3
res = 0

arr = [2,3,5,4,6]
arr.reverse()
first = arr[0]
second = arr[1]

while(m!=0):
    if(m>k):
        res += first * k
        m -= k
    elif(m >0):
        res += first * m
        m = 0

    if(m>k):
        res += second
        m -= 1

print(res)   
