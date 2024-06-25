# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def doubleIt(self, head):
        # Reverse the linked list
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        print("After reversing the linked list:")
        self.printLinkedList(prev)

        # Double the values and handle carryovers
        current=prev
        rem=0
        while current or rem:
            current.val=current.val*2+rem
            rem=current.val//10
            print(rem)
            current.val=current.val%10
            if current.next is None and rem>0:
                current.next=ListNode(rem)
                break
            current = current.next

        print("After doubling the values and handling carryovers:")
        self.printLinkedList(prev)

        # Reverse the linked list again
        current = prev
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        print("After reversing the linked list again:")
        self.printLinkedList(previous)

        return previous

    def printLinkedList(self, head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


# Testing the code with the provided input [9,9,9]
head = ListNode(9)
head.next = ListNode(9)
head.next.next = ListNode(9)

sol = Solution()
result = sol.doubleIt(head)
print("Final result:")
sol.printLinkedList(result)
