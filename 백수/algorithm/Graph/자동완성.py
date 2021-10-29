import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
def make_trie(root,word):
    cur_node=root
    for c in word:
        if c not in cur_node[1]:
            cur_node[1][c]=[0,dict()]

        cur_node[0]+=1
        cur_node=cur_node[1][c]
    cur_node[0]+=1
def search_target(root,word):
    ret=0
    cur_node=root
    
    for c in word:
        if cur_node[0]==1:
            return ret
        ret+=1
        cur_node=cur_node[1][c]

    return ret
def solution(words):
    answer = 0
    root=[0,dict()]
    
    for word in words:
        make_trie(root,word)
    for word in words:
        answer += search_target(root,word)

    return answer