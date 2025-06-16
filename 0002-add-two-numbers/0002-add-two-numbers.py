# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        temp = head
        carry = 0

        while (l1 is not None) or (l2 is not None) or carry != 0:
            num1 = l1.val if (l1 is not None) else 0
            num2 = l2.val if (l2 is not None) else 0

            result = num1 + num2 + carry
            carry = result // 10
            value = result % 10

            temp.next = ListNode(value)
            temp = temp.next

            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        return head.next