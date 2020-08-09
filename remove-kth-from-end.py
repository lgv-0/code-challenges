# Write a function that receives as input the head node of a linked list and an integer k.
# Your function should remove the kth node from the end of the linked list and return the head node of the updated list.
#
# For example, if we have the following linked list: 
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (14) -> (13) -> (12) -> (11) -> null
#
# The head node would refer to the node (20).  Let k = 4, so our function should remove the 4th node from the end of the linked list, the node (14).
#
# After the function executes, the state of the linked list should be:
# (20) -> (19) -> (18) -> (17) -> (16) -> (15) -> (13) -> (12) -> (11) -> null
#
# If k is longer than the length of the linked list, the linked list should not be changed.

# My solution involves using a "queue" like structure to reserve the previous nodes that were iterated over until you reach
# the end of the list.

def remove_kth_from_end(head, k):
    if k == 0:
        return head
    
    # Need to traverse the linked list
    # Keeping track of the past k nodes + 1
    leng = 0
    node_holder = []
    cur_node = head
    while cur_node != None:
        leng = leng + 1
        
        # Remove the 1st element in our
        # container to make room for the next
        # (IF length is too long now)
        if node_holder.__len__() == k + 1:
            node_holder.pop(0)
        
        # Add this node to the container
        node_holder.append(cur_node)
        
        cur_node = cur_node.next
        
    # If length is less than 2 or length is
    # less than k our list is way too small
    if node_holder.__len__() < 2 or leng < k:
        return head
    
    if node_holder.__len__() > 2:
        node_holder[0].next = node_holder[2]
        del node_holder[1]
    elif k == 1:
        node_holder[0].next = None
        del node_holder[1]
    else:
        node_holder.pop(0)
        return node_holder[0]
    
    return head