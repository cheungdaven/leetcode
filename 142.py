# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        meet_node = None
        while fast and slow and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meet_node = slow
                break

        if meet_node:
            p = head
            q = meet_node
            while p and q:
                if p is q:
                    return p
                p = p.next
                q = q.next

        return None