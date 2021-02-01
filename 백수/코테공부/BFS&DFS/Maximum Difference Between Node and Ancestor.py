# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node):
        #리프노드일 경우
        if node.left == None and node.right == None:
            return [node.val],0
        #현재 노드의 값을 ans에 배열형태로 저장
        ans = [node.val]
        max_val = 0

        #왼쪽자식이 있을 경우
        if node.left != None:
            #왼쪽 탐색
            tmp,num = self.dfs(node.left)
            max_val = max(max_val,num)
            ans.extend(tmp)
            tmp.extend([node.val])
            max_val = max(abs(max(tmp) - node.val), abs(node.val- min(tmp)), max_val)
        #오른쪽자식이 있을 경우
        if node.right != None:
            #오른쪽 탐색
            tmp,num = self.dfs(node.right)
            max_val = max(max_val,num)
            ans.extend(tmp)
            tmp.extend([node.val])
            max_val = max(abs(max(tmp) - node.val), abs(node.val- min(tmp)), max_val)
        
        return ans,max_val
    def maxAncestorDiff(self, root: TreeNode) -> int:
        _,ans = self.dfs(root)
        
        return ans