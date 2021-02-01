############################################################################################
#1457. Pseudo-Palindromic Paths in a Binary Tree                                           #
#https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/                  #
############################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,path,ans):
        #현재 노드를 path에 추가
        path.append(node.val)
        
        #리프노드일 경우
        if node.left == None and node.right == None:
            return ans.append(path)
        
        #path를 그냥 인자로 넣어주면 얕은복사가 되므로 path[:]로 넘겨준다
        #path + [node.val]을 인자로 넘겨주는것도 가능
        if node.left != None:
            self.dfs(node.left,path[:],ans)
        if node.right != None:
            self.dfs(node.right,path[:],ans)
            
        return ans
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        #루트밖에 없는 경우 처리
        if root.left == None and root.right == None:
            return 1
        
        ans = 0
        #경로를 반환 받아서 pseudo-palindromic 가 되는지 확인
        for arr in self.dfs(root, [],[]):
            #개수를 세기 위해 set으로 중복 제거
            group = list(set(arr))
            #같은 수의 개수가 홀수 이면 cnt 증가
            cnt = 0
            for i in group:
                if arr.count(i) % 2 != 0:
                    cnt += 1
                if cnt > 1:
                    break
            #개수가 홀수인 값이 2개 이상이면 대칭되도록 만들수 없으므로 ans += 1
            if cnt < 2:
                ans += 1
                
        return ans
                
                