"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single 
digit. Add the two numbers and return it as a linked list.You may assume the 
two numbers do not contain any leading zero, except the number 0 itself.
Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
""" 

#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def arry_to_ln(alist):
    root = ListNode(alist[0])
    result = root
    for index, value in enumerate(alist):
        if index > 0:
            root.next = ListNode(value)
            root = root.next
    return result

def print_ln(ln):
    if ln:
        while ln:
            print(ln.val,end=' ')
            ln = ln.next

print_ln(arry_to_ln([2,3,5,6]))


class Solution:
    def addTwoNumbers(self, l1, l2):
        root = ListNode(1)
        result = root
        carry = 0
        
        while l1 or l2 or carry == 1:
            value = 0
            if l1:
                value +=l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            value += carry
            root.next = ListNode(value%10)
            carry = value//10
            root = root.next
            #print(value, result)
        return result.next

#A = Solution
#A.addTwoNumbers([2,4,3],[5,4,6])