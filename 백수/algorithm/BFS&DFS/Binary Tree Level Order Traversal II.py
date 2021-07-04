##########################################################################################
#107. Binary Tree Level Order Traversal II                                               #
#https://leetcode.com/problems/binary-tree-level-order-traversal-ii/                     #
##########################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#큐 사용
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        #빈 트리가 입력될 경우
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        
        #큐가 빌때까지 탐색한다. ==> 모두 탐색
        while queue:
            #같은 레벨의 노드를 하나의 리스트에 담기 위해 사용
            current_level_node = []
            #다음 레벨 노드들을 담기 위해 사용
            next_node = []

            for node in queue:
                #현재 큐에 있는 노드들은 같은 레벨이므로 값들을 넣어준다.
                current_level_node.append(node.val)
                #현재 노드의 자식노드들을 담아준다
                for child in (node.left,node.right):
                    #None이 아닐 경우에만 담아준다
                    if child:
                        next_node.append(child)
            
            #큐를 다음 노드 리스트로 바꿔준다
            queue = next_node
            #정답 리스트에 append
            ans.append(current_level_node)
        
        #뒤집어서 반환
        #reversed(ans)도 가능하다
        return ans[::-1]