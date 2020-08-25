# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, val=0) -> ListNode:
        node_1_val = l1.val + l2.val + val // 10
        modded_val = node_1_val % 10
        node1 = ListNode(modded_val)
    
        if l1.next is not None or l2.next is not None:
            node1.next = self.addTwoNumbers(l1.next, l2.next, node_1_val)

        return node1