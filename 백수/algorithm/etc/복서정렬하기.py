def solution(w, h):
    ans = []
    answer = []
    for i in range(len(h)):
        win,loss,score = 0,0,0
        for j in range(len(h[i])):
            if h[i][j] == 'W':
                win+=1
                if w[i] < w[j]:
                    score+=1
            elif h[i][j] == 'L':
                loss+=1
        tmp = 0
        if win!=0:
            tmp = win/(win+loss)
        ans.append([tmp,score,w[i],i])
    ans = sorted(ans,key=lambda x:(-x[0],-x[1],-x[2],x[3]))
    for a in ans:
        answer.append(a[3]+1)
    
    return answer