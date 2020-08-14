# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order and each of their nodes contain a single digit. 
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nextList = None
        lastNode = None
        
        list1array = []
        list2array = []
        
        tmpBuild = l1
        while tmpBuild is not None:
            list1array.append(tmpBuild.val)
            tmpBuild = tmpBuild.next
        
        tmpBuild = l2
        while tmpBuild is not None:
            list2array.append(tmpBuild.val)
            tmpBuild = tmpBuild.next
        
        newList = None
        carry = 0
        iterations = 0
        while True:
            nextNumber = carry
            if len(list1array) > iterations:
                nextNumber = nextNumber + list1array[iterations]
            if len(list2array) > iterations:
                nextNumber = nextNumber + list2array[iterations]
                
            if nextNumber == 0 and len(list1array) < iterations + 1 and len(list2array) < iterations + 1:
                break
            
            carry = 0
            iterations = iterations + 1
            
            while nextNumber > 9:
                carry = carry + 1
                nextNumber = nextNumber - 10
            
            if nextList is None:
                nextList = ListNode(nextNumber)
                lastNode = nextList
            else:
                lastNode.next = ListNode(nextNumber)
                lastNode = lastNode.next
        
        if nextList is None:
            nextList = ListNode(0)
        
        return nextList