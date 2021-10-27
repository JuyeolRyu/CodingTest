def solution(files):
    answer = []
    for idx,file in enumerate(files):
        head,number,tail='','',''
        for i,c in enumerate(file):
            if not c.isdigit():
                head+=c
            else:
                for j in range(i,len(file)):
                    if file[j].isdigit():
                        number+=file[j]
                    else:
                        tail=file[j:]
                        break
                break
        answer.append([head,number,tail,idx])
        
    answer=sorted(answer,key=lambda x:(x[0].lower(),int(x[1]),x[3]))
    answer=list(map(lambda x:x[0]+x[1]+x[2],answer))
    return answer