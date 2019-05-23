# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current, previous = head, None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous