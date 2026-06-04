# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = []
        while head and not head in seen:
            seen.append(head)
            head = head.next
        if head:
            return True
        else:
            return False