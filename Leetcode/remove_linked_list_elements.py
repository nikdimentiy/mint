# LeetCode problem: 203
# https://leetcode.com/problems/remove-linked-list-elements/description/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Removes all nodes with the given value from the linked list.

        Parameters:
        - head (Optional[ListNode]): The head of the linked list.
        - val (int): The value to be removed.

        Returns:
        - Optional[ListNode]: The new head of the modified linked list.
        """
        # Create a dummy node to handle the edge case of removing the head
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        # Traverse the linked list
        while current.next:
            # Check if the next node has the specified value
            if current.next.val == val:
                # Remove the node by updating the next pointer
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next

        return dummy.next


# Example usage:
# Example 1:
head1 = ListNode(
    1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
)
val1 = 6
solution1 = Solution()
result1 = solution1.removeElements(head1, val1)
# Output: [1, 2, 3, 4, 5]

# Example 2:
head2 = None
val2 = 1
solution2 = Solution()
result2 = solution2.removeElements(head2, val2)
# Output: []

# Example 3:
head3 = ListNode(7, ListNode(7, ListNode(7, ListNode(7))))
val3 = 7
solution3 = Solution()
result3 = solution3.removeElements(head3, val3)
# Output: []
