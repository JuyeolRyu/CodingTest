def solution(s):
    answer = ''
    dic={'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}
    tmp_s=''
    for c in s:
        tmp_s+=c
        if c.isdigit():
            answer+=c
            tmp_s=''
            continue
            
        if tmp_s in dic:
            answer+=dic[tmp_s]
            tmp_s=''
    
    return int(answer)