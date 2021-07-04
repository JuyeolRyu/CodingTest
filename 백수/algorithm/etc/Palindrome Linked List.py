# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        
        node = head
        lst = []
        while True:
            lst.append(node.val)
            
            if node.next == None:
                break
            node = node.next
            
        a = lst[:len(lst)//2]
        b = lst[len(lst)//2:]
        b.reverse()

        for i in range(len(a)):
            if a[i] != b[i]:
                return False
            
        return True