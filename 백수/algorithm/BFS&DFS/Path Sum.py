
############################################################################
#112. Path Sum                                                             #
#https://leetcode.com/problems/path-sum/                                   #
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node,ans,sum):
        #리프노드이고 val의 합이 목표값과 같을때
        if node.left == None and node.right == None and node.val+ans == sum:
            return True
        
        check = False
        
        #리프노드아닐때
        if node.left != None:
            check = check or self.dfs(node.left, ans + node.val, sum)
        if node.right != None:
            check = check or self.dfs(node.right, ans + node.val, sum)
        
        return check
    
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False
        
        return self.dfs(root,0,sum)