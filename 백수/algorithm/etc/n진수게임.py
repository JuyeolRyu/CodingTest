#https://programmers.co.kr/learn/courses/30/lessons/17687
dic={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
def decToN(dec,n):
    ret=''
    while dec>0:
        dec,mod=dec//n,dec%n
        if mod in dic:
            ret+=dic[mod]
        else:
            ret+=str(mod)
    
    return ret[::-1]
def solution(n, t, m, p):
    ans=''
    s = '0'
    number=1

    while len(s)<t*m:
        s+=decToN(number,n)
        number+=1
    while len(ans)<t:
        ans+=s[p-1]
        p+=m
    return ans