##########################################################################################
#110. Balanced Binary Tree                                                               #
#https://leetcode.com/problems/balanced-binary-tree/                                     #
##########################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,tree):
        #왼쪽과 오른쪽 트리의 높이 저장
        left = right = 0
        #자식 노드가 없는 경우
        if tree.left == None and tree.right == None:
            return 1
        
        #높이 측정 dfs
        if tree.left != None:
            left = self.dfs(tree.left)
        if tree.right != None:
            right = self.dfs(tree.right)
            
        #왼쪽과 오른쪽의 높이 차이가 2 이상인 경우 
        #왼쪽 오른쪽 서브트리중 불균형 서브트리가 있는 경우 -1 반환 
        if abs(left - right) > 1 or left == -1 or right == -1:
            return -1
        #서브트리들이 균형 트리인 경우 높이 +1 반환
        return max(left,right)+1
            
        
    def isBalanced(self, root: TreeNode) -> bool:
        #빈 배열이면 True 반환
        if not root:
            return True
        
        #트리가 불균형 트리인 경우
        if self.dfs(root) == -1:
            return False
        #트리가 균형 트리인 경우
        return True
        
        