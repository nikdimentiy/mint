// LeetCode task: solution -> https://leetcode.com/problems/merge-two-sorted-lists/description/

package main

import (
	"fmt"
	"math"
)

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	// Create a dummy node as the head of the merged list
	dummy := &ListNode{Val: math.MinInt32}
	current := dummy
	ptr1 := list1
	ptr2 := list2

	// Iterate through both lists
	for ptr1 != nil && ptr2 != nil {
		if ptr1.Val <= ptr2.Val {
			current.Next = ptr1
			ptr1 = ptr1.Next
		} else {
			current.Next = ptr2
			ptr2 = ptr2.Next
		}
		current = current.Next
	}

	// Append remaining nodes
	if ptr1 != nil {
		current.Next = ptr1
	}
	if ptr2 != nil {
		current.Next = ptr2
	}

	return dummy.Next
}

func main() {
	// Example usage
	list1 := &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4}}}
	list2 := &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4}}}

	mergedList := mergeTwoLists(list1, list2)
	current := mergedList
	for current != nil {
		fmt.Print(current.Val, " ")
		current = current.Next
	}
}
