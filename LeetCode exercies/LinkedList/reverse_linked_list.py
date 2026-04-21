# Definition of SinglyLinkedListNode
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

# Iterative Solution
class Solution(object):
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next

        return prev

# Recursive solution
class Solution(object):
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
