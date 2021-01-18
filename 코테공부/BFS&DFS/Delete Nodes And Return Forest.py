# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        #dfs탐색 메소드
        def dfs(node):
            #left child가 있을 경우
            if node.left != None:
                #left child의 val가 삭제 리스트에 있을경우
                if node.left.val in to_delete:
                    root_arr.append(node.left)
                    node.left = None
                #없을경우 계속 탐색
                else:
                    dfs(node.left)
            if node.right != None:
                if node.right.val in to_delete:
                    root_arr.append(node.right)
                    node.right = None
                else:
                    dfs(node.right)
                    
            return;
        
        ans = []
        root_arr = [root]
        
        while root_arr:
            #리스트의 첫번째 값을 꺼낸다
            root = root_arr.pop(0)
            #꺼낸 트리의 val가 삭제리스트에 있는 경우 child를 채워넣는다
            if root.val in to_delete:
                if root.left != None:
                    root_arr.append(root.left)
                if root.right != None:
                    root_arr.append(root.right)
            #없는 경우
            else:
                #꺼낸 노드를 ans에 넣어주고 탐색 시작
                ans.append(root)
                dfs(root)
            
        return ans