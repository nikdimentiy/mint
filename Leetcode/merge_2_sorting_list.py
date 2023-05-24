# LeetCode task: solution -> https://leetcode.com/problems/merge-two-sorted-lists/description/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists and return the head of the merged list.

        Args:
            list1: The head of the first sorted linked list.
            list2: The head of the second sorted linked list.

        Returns:
            The head of the merged sorted linked list.
        """
        # Create a dummy node as the head of the merged list
        dummy = ListNode(0)
        # Create a pointer to track the current node of the merged list
        current = dummy
        # Create two pointers to track the nodes of the input lists
        ptr1 = list1
        ptr2 = list2
        # Iterate through both lists until one of them is exhausted
        while ptr1 and ptr2:
            # Compare the values of the current nodes and append the smaller one to the merged list
            if ptr1.val <= ptr2.val:
                current.next = ptr1
                # Move the pointer of the first list to the next node
                ptr1 = ptr1.next
            else:
                current.next = ptr2
                # Move the pointer of the second list to the next node
                ptr2 = ptr2.next
            # Move the pointer of the merged list to the next node
            current = current.next
        # Append remaining nodes if any
        if ptr1:
            current.next = ptr1
        if ptr2:
            current.next = ptr2
        # Return the head of the merged list, skipping the dummy node
        return dummy.next
