############################################################################
#199. Binary Tree Right Side View                                          #
#https://leetcode.com/problems/binary-tree-right-side-view/                #
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        #빈 루트가 주어질 경우 제외
        if root:
            ans = [root.val]
        else:
            return None
        #deque에 추가
        q = deque([root])

        while q:
            #bfs 할때마다 각 레벨을 구분하기 위해 deque 하나 더 사용
            tmp_q = deque()
            while q:
                node = q.popleft()
                #빈 노드가 아닌 경우
                if node:
                    if node.left:
                        tmp_q.append(node.left)
                    if node.right:
                        tmp_q.append(node.right)
            #이번 레벨에 노드가 있는 경우 ans에 마지막 val 추가
            if tmp_q:
                ans.append(tmp_q[-1].val)
            #큐를 최신화
            q = tmp_q
            
        return ans