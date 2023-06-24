# LeetCode task: solution -> https://leetcode.com/problems/add-two-numbers/description/
# 🎯 Preparation to coding interview 🍀


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        This function takes two linked lists representing non-negative integers and returns a linked list representing their sum.
        The digits are stored in reverse order and each node contains a single digit.

        Example:
        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [7,0,8]
        Explanation: 342 + 465 = 807.

        Parameters:
        l1: Optional[ListNode] - the first linked list
        l2: Optional[ListNode] - the second linked list

        Returns:
        Optional[ListNode] - the sum of the two linked lists as a new linked list
        """
        dummy = ListNode(0) # create a dummy node to start the result list
        curr = dummy # create a pointer to the current node of the result list
        carry = 0 # initialize the carry value to zero

        while l1 or l2: # loop until both lists are exhausted
            x = l1.val if l1 else 0 # get the value of the current node of l1 or zero if l1 is None
            y = l2.val if l2 else 0 # get the value of the current node of l2 or zero if l2 is None
            _sum = x + y + carry # calculate the sum of the two values and the carry
            carry = _sum // 10 # update the carry value to be the quotient of the sum divided by 10
            curr.next = ListNode(_sum % 10) # create a new node with the remainder of the sum modulo 10 and append it to the result list
            curr = curr.next # move the pointer to the next node of the result list

            if l1: # if l1 is not None
                l1 = l1.next # move to the next node of l1
            if l2: # if l2 is not None
                l2 = l2.next # move to the next node of l2

        if carry > 0: # if there is still a non-zero carry value after both lists are exhausted
            curr.next = ListNode(carry) # create a new node with the carry value and append it to the result list

        return dummy.next # return the head of the result list (skipping the dummy node)
