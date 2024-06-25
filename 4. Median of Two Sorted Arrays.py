class Solution:
    def getBinaryValue(self, head) -> str:
        s = ''
        current = head
        while current:
            s = s + str(current.val)
            current = current.next
        return int(s,2)  # Return binary representation, excluding the '0b' prefix
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating a linked list: 1 -> 0 -> 1
head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)
solution = Solution()
binary_value = solution.getBinaryValue(head)
print(binary_value)
