# import time

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# innermost = ListNode(7 , None)
# lnode_inner = ListNode(6 , innermost)
# lnode= ListNode(4 , lnode_inner)


# l1_content = []

# while True:
#     if lnode.next is None:
#         l1_content.insert(0 , lnode.val)
#         break

#     l1_content.insert(0, lnode.val)
#     lnode = lnode.next


# l1_copy = l1_content.copy()
# num = str(int(''.join(str(i) for i in l1_content)))

# for i in range(-1 , -(len(num) + 1), -1):
#     if i == -1:
#         n_one_to_last = None
#         n_last = ListNode(int(num[i]))
      
#     else:
#         n_one_to_last = n_last
#         n_last = ListNode(int(num[i]), n_one_to_last)
 



# gpt suggested
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Placeholder for the result list
        current = dummy_head  # Pointer to build the new list
        carry = 0  # Initialize carry to 0

        # Loop until both lists are processed and no carry remains
        while l1 is not None or l2 is not None or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 or 0 if l1 is None
            val2 = l2.val if l2 else 0  # Get value from l2 or 0 if l2 is None
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for next iteration
            current.next = ListNode(total % 10)  # Create new node for the result
            current = current.next  # Move to the next node
            
            # Move to the next nodes in l1 and l2 if possible
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next  # Return the next node after the dummy head