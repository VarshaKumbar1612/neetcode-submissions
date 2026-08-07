# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # l = len(head)
        # for i in range(l-1):
        #     temp = head[i]
        #     head[i] = head[l-1-i]
        #     head[l-1-i] = temp
        # return head 
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev 
