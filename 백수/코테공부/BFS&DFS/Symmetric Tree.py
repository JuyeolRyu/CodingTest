############################################################################
#101. Symmetric Tree                                                       #
#https://leetcode.com/problems/symmetric-tree/                             #
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        #루트가 비었거나 자식들이 없는 경우
        if not root or not root.left and not root.right:
            return True
        
        #자식이 한쪽만 없는 경우
        if root.left == None or root.right == None:
            return False
        
        #왼쪽 먼저 탐색
        queue = deque([root.left])
        
        left = []
        #대칭을 비교하기 위해 왼쪽 먼저 탐색하고 오른쪽 탐색
        while queue:
            node = queue.popleft()
            #현재 노드가 빈 노드이면 None append 하고 다음 노드로 넘어간다
            #빈 노드가 아니라면 탐색 계속
            if node == None:
                left.append(None)
            else:
                left.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        #오른쪽 탐색
        queue = deque([root.right])
        
        right = []
        #대칭을 비교하기 위해 오른쪽 먼저 탐색하고 왼쪽 탐색
        while queue:
            node = queue.popleft()
            
            if node == None:
                right.append(None)
            else:
                right.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
        #값 비교
        for idx in range(len(left)):
            if left[idx] != right[idx]:
                return False
        
        return True     