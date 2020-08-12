# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) 
# in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        if head.next is None:
            return None
        
        cur = head
        nodeDict = set()
        while cur is not None:
            if cur in nodeDict:
                return cur
            
            nodeDict.add(cur)
            cur = cur.next
            
        return None