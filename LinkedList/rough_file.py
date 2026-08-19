# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None

        list1 = head
        curr = slow

        list2_prev = None

        while curr:
            nextNode = curr.next
            curr.next = list2_prev
            list2_prev = curr
            curr = nextNode
        
        list2 = list2_prev

        while list2:

            n1 = list1.next
            n2 = list2.next
            list1.next = list2
            list2.next = n1
            list1 = n1
            list2 = n2

        print(list1)
        print(list2)

        
        

        return head



        








        
