'''
트리
https://www.acmicpc.net/problem/1068
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

def make_tree(arr,target):
    tree = defaultdict(list)
    for parent,me in arr:
        if me != target:
            tree[parent].append(me)

    tree[target] = []
    return tree

def dfs(cur):
    global ans
    if not tree[cur]:
        ans += 1
        return

    for ne in tree[cur]:
        dfs(ne)
    return
ans = 0
n = int(input())
tree = list(map(int,input().split()))
target = int(input())
for i in range(len(tree)):
    tree[i] = [tree[i],i]

tree = make_tree(tree,target)
if not tree[-1]:
    print(0)
else:
    dfs(-1)
    print(ans)

'''
12
1 4 3 -1 3 1 2 0 6 6 6 1
2
'''