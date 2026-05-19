# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        n = self.length(headA)
        m = self.length(headB)
        first = headA
        second = headB

        if m <= n:
            for i in range(n-m):
                first = first.next
        else:
            for i in range(m-n):
                second = second.next
        
        while first is not None:
            if(first == second):
                return first
            first = first.next
            second = second.next
        
        return None


    def length(self,head):
        x = 0
        curr = head
        while(curr is not None):
            curr = curr.next
            x += 1
    
        return x