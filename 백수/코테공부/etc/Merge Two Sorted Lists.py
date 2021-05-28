# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        answer = ListNode()
        ans = answer
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
            
        if l1 == None:
            ans.next = l2
        else:
            ans.next = l1

        return answer.next