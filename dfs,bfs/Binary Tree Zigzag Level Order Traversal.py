############################################################################
#103. Binary Tree Zigzag Level Order Traversal                             #
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/  #
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#마지막에 리스트 뒤집어 주면 된다
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            tmp_queue = deque()
            tmp_list = []
            for node in queue:
                tmp_list.append(node.val)
                if node.left != None:
                    tmp_queue.append(node.left)
                
                if node.right != None:
                    tmp_queue.append(node.right)
        
            queue = tmp_queue
            ans.append(tmp_list)
        
        for i in range(1,len(ans),2):
            ans[i].reverse()
            
        return ans