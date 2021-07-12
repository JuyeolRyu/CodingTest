#사이클 게임
#https://www.acmicpc.net/problem/20040

#sol1(kruskal)
'''
그래프 연결할때마다 그래프 사이클 검사
'''
import sys
input = sys.stdin.readline
def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x<y:
        parent[y] = x
    else:
        parent[x] = y

ans = 0
n,m = map(int,input().split())
parent = [i for i in range(n)]
edge = [list(map(int,input().split())) for _ in range(m)]
for i,e in enumerate(edge):
    a,b = e[0],e[1]
    if find(a) == find(b):
        ans = i+1
        break
    else:
        union(a,b)
    
print(ans)