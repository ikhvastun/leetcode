from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        """Returns a string representation of the linked list."""
        values = [str(self.val)]  # Start with the current node's value
        current = self  
        while current.next:
            current = current.next
            values.append(str(current.val))
        return " -> ".join(values)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = [] 
        
        memory = 0

        dummy = ListNode()
        res = dummy

        while l1 or l2 or memory:

            sum = memory
            
            if l1: 
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            # sum = l1_value + l2_value
            rem = sum % 10
            full = sum // 10
            dummy.next = ListNode(rem)
            dummy = dummy.next
            result.append(rem)

            if full > 0:
                memory = 1
            else:
                memory = 0

        return res.next


def lst2link(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next


if __name__ == "__main__":
    sol = Solution()
    first = [1, 2, 3]
    second = [1, 2, 3, 4]
    l1 = lst2link(first)
    l2 = lst2link(second)

    added = sol.addTwoNumbers(l1, l2)

    while added:
        print(added.val, end="")
        added = added.next
    print()      