############################################################################
#865. Smallest Subtree with all the Deepest Nodes                          #
#https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/#
############################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node):
            ans = 0
            #리프노드일 경우 1반환
            if node.left == None and node.right == None:
                return 1
            #왼쪽과 오른쪽 중 최대 깊이를 구한다
            if node.left != None:
                ans = max(ans,dfs(node.left)+1)
            if node.right != None:
                ans = max(ans,dfs(node.right)+1)
            #최대 깊이 반환
            return ans
        
        #빈트리일 경우
        if not root:
            return None
        #자식이 없을 경우
        if root.left == None and root.right == None:
            return root
        while True:
            left_depth = 0
            right_depth = 0
            #한쪽 자식이 없을 경우를 위해 조건 추가
            if root.left != None:
                left_depth = dfs(root.left)
            if root.right != None:
                right_depth = dfs(root.right)
                
            #양쪽 깊이가 같으면 현재 노드 반환
            if left_depth == right_depth:
                ans = root
                break
            #왼쪽이 깊으면 왼쪽으로
            elif left_depth > right_depth:
                root = root.left
            #오른쪽이 깊으면 오른쪽으로
            else:
                root = root.right
        
        return ans