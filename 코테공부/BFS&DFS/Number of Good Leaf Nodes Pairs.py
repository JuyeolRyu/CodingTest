############################################################################################
#1530. Number of Good Leaf Nodes Pairs                                                     #
#https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/                            #
############################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        q = deque()
        q.append(root)
        #트리를 배열로 만들기 위해 생성,루트 값을 1로 지정
        tree_lst = []
        root.val = 1
        #트리 배열로 만들기,bfs 탐색
        while q:
            node = q.popleft()
            #node가 none이 아닌 경우
            if node:
                #left 탐색하고 val 값을 바꿔줌
                if node.left != None:
                    q.append(node.left)
                    node.left.val = node.val*2
                #right 탐색하고 val 값을 바꿔줌
                if node.right != None:
                    q.append(node.right)
                    node.right.val = node.val*2+1
                #leaf 노드인 경우
                if node.left == None and node.right == None:
                    tree_lst.append(node.val)

        ans = []
        #다른 리프노드와의 거리를 계산한다
        for i in range(len(tree_lst)):
            for j in range(i+1,len(tree_lst)):
                a,b = [tree_lst[i],tree_lst[j]]
                cnt = 0
                while a != b:
                    if a>b:
                        a = a//2
                        cnt += 1
                    elif a < b:
                        b = b//2
                        cnt += 1
                    #distance보다 길어지면 중지
                    if cnt > distance:
                        break
                #distance보다 짧은 것만 ans에 추가한다
                if cnt <= distance:
                    ans.append(cnt)
        
        return len(ans)