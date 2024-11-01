from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy
        quotient = 0
        while l1 or l2 or quotient:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            quotient, remainder = divmod(l1val + l2val + quotient, 10)
            newNode = ListNode(remainder)
            result.next = newNode
            result = newNode
            l1 = l1.next if l1 else False
            l2 = l2.next if l2 else False
        return dummy.next


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
