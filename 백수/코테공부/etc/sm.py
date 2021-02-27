######################################
#1
def search(dic,cur,ans):
    if cur not in dic:
        print(ans)
        return;
    for n in dic[cur]:
        search(dic,n,ans+' '+n)
    dic[cur] = []
    return
def main():
    k = input().split()
    n = int(input())
    dic = {}
    for i in range(n):
        x,y = input().split()
        if x not in dic:
            dic[x] = [y]
        else:
            dic[x].append(y)

    for i in dic:
        search(dic,i,i)
if __name__=="__main__":
    main()


######################################
#2
def main():
    p,n,h = map(int,input().split())
    dic = {}
    ans = []
    for i in range(n):
        x,y = map(int,input().split())
        if x not in dic:
            dic[x] = [y]
        else:
            dic[x].append(y)
    for i in dic:
        num = 0
        dic[i] = sorted(dic[i])
        print(i,dic[i])
        for j in dic[i]:
            if num+j <= h:
                num += j
            else:
                break
        ans.append(str(i) +' '+ str(num*1000))
    
    for s in ans:
        print(s)
    

if __name__=="__main__":
    main()





###
def main():
    p,n,h = map(int,input().split())
    dic = {}
    ans = []
    for i in range(n):
        x,y = map(int,input().split())
        if x not in dic:
            dic[x] = [y]
        else:
            dic[x].append(y)
    for i in dic:
        dic[i] = sorted(dic[i],reverse = True)
        num = 0
        dp = [0 for i in range(h+1)]
        
        for j in dic[i]:
            print(j)
            if j > h:
                continue
            else:
                for k in range(h,1,-1):
                    if dp[k-j]  != 0:
                        dp[k] = max(dp[k],dp[k-j]+j)
                    elif k == j:
                        dp[k] = k
        print(dp)
        ans.append(max(dp))
    
    for s in ans:
        print(s)
    

if __name__=="__main__":
    main()




######################################
#5
def main():
    n = int(input())
    dic = {}
    for i in range(n**2):
        li = list(map(int,input().split()))
        
        for t in li[2:]:
            if t not in dic:
                dic[t] = [li[0]]
            else:
                dic[t].append(li[0])
    
    ans = 0
    for i in dic:
        ans += max(dic[i])
    print(ans)


if __name__=="__main__":
    main()

######################################
#4
from collections import deque
def main():
    x = int(input())
    li = list(map(int,input().split()))
    visited = [False for i in range(len(li))]
    
    q = deque()
    q.append(li[0])
    idx = 0
    cnt = 1
    visited[idx] = True
    while q:
        cur = q.popleft()

        if visited[idx+cur]:
            print(cnt+1)
            break
        visited[idx+cur] = True
        
        
        idx += cur
        cnt += 1
        q.append(li[idx])


if __name__=="__main__":
    main()


######################################
#7
select o.buyer_id,o.buy_date,l.book_name,l.price
from library as l,orderInfo as o
where l.book_name = 'Looking with Elice' or o.buy_date between '2020-07-27' and'2020-07-31'
order by o.buy_date asc;