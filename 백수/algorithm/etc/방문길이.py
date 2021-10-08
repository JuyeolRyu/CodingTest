def solution(dirs):
    answer = set()
    x,y = 0,0
    dic={'L':[-1,0],'R':[1,0],'U':[0,1],'D':[0,-1]}
    
    for d in dirs:
        dx,dy = dic[d]
        if -5<=x+dx<=5 and -5<=y+dy<=5:
            answer.add(str(x)+str(y)+str(x+dx)+str(y+dy))
            answer.add(str(x+dx)+str(y+dy)+str(x)+str(y))
            x+=dx
            y+=dy

    return len(answer)//2