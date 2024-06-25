class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Input lists
l1 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l2 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))

# Create a Solution instance
solution = Solution()

# Call the addTwoNumbers function
result = solution.addTwoNumbers(l1, l2)

# Print the result
while result:
    print(result.val, end=" ")
    result = result.next
