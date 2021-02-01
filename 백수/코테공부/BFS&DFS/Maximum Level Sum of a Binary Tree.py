############################################################################
#1161. Maximum Level Sum of a Binary Tree                                  #
#https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/         #
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        ans_list = []
        queue = deque()
        queue.append(root)
        
        while queue:
            tmp_queue = deque()
            tmp_sum = 0
            for node in queue:
                tmp_sum += node.val
                
                if node.left != None:
                    tmp_queue.append(node.left)
                    
                if node.right != None:
                    tmp_queue.append(node.right)
            queue = tmp_queue
            ans_list.append(tmp_sum)
            
        return ans_list.index( max(ans_list))+1