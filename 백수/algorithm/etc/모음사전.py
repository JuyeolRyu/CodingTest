def solution(word):
    answer = 0
    li = ['','A','E','I','O','U']

    my_str = []
    for i in range(1,6):
        s1 = li[i]
        for j in range(6):
            s2 = s1+li[j]
            for k in range(6):
                s3 = s2+li[k]
                for l in range(6):
                    s4 = s3+li[l]
                    for m in range(6):
                        s5 = s4+li[m]
                        my_str.append(s5)
            
    my_str = list(set(my_str))
    my_str.sort()
    answer=my_str.index(word)+1
    return answer