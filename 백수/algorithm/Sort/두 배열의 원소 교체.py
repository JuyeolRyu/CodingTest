###################################################################
#두 배열의 원소 교체                                               #
#n,k 와 두 리스트 a,b를 입력받는다                                 #
#k번 만큼 a,b 값을 교환하는데 a의 모든원소의 합이 최대가 되도록한다  #
###################################################################
n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a = sorted(a)
b = sorted(b,reverse=True)
ans = 0
for i in range(n):
  if i < k:
    ans += b[i]
  else:
    ans += a[i]
  
print(ans)