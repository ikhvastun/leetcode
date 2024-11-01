import unittest
from main import ListNode, Solution  # Assuming your code is in 'main.py'

class TestAddTwoNumbers(unittest.TestCase):

    def test_add_two_numbers_1(self):
        l1 = ListNode(2, ListNode(4, ListNode(3)))  # [2,4,3]
        l2 = ListNode(5, ListNode(6, ListNode(4)))  # [5,6,4]
        expected = [7, 0, 8]  # Expected output as a list
        self.assertEqual(self.list_to_array(Solution().addTwoNumbers(l1, l2)), expected)

    def test_add_two_numbers_2(self):
        l1 = ListNode(0)  # [0]
        l2 = ListNode(0)  # [0]
        expected = [0]  # Expected output as a list
        self.assertEqual(self.list_to_array(Solution().addTwoNumbers(l1, l2)), expected)

    def test_add_two_numbers_3(self):
        l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))  # [9,9,9,9,9,9,9]
        l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))  # [9,9,9,9]
        expected = [8, 9, 9, 9, 0, 0, 0, 1]  # Expected output as a list
        self.assertEqual(self.list_to_array(Solution().addTwoNumbers(l1, l2)), expected)

    # Helper function to convert ListNode to an array for comparison
    def list_to_array(self, head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

if __name__ == '__main__':
    unittest.main()
