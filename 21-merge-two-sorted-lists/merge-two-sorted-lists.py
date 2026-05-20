# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = None
        tail = None

        while(p1 is not None or p2 is not None):
            data = None
            if (p1 is not None and p2 is not None):
                if(p1.val <= p2.val):
                    data = p1.val
                    p1 = p1.next
                else:
                    data = p2.val
                    p2 = p2.next
            elif(p1 is not None):
                data = p1.val
                p1 = p1.next
            else:
                data = p2.val
                p2 = p2.next
            
            if tail is None:
                head = self.insertAtLast(tail, data)
                tail = head
            else:
                tail = self.insertAtLast(tail, data)
        return head
    
    def insertAtLast(self,tail,data):
        newNode = ListNode(data)
        if tail is not None:
            tail.next = newNode
        return newNode
        