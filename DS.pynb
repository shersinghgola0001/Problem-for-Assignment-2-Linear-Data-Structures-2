#Q1. Delete the elements in an linked list whose sum is equal to zero.

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_zero_sum_sublists(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    prefix_sum = 0
    prefix_sums = {}  # Store prefix sums along with corresponding node
    
    while current:
        prefix_sum += current.value
        
        if prefix_sum in prefix_sums:
            # Remove nodes between prefix_sums[prefix_sum] and current
            prev = prefix_sums[prefix_sum].next
            temp_sum = prefix_sum
            
            while prev != current:
                temp_sum += prev.value
                del prefix_sums[temp_sum]
                prev = prev.next
            
            prefix_sums[prefix_sum].next = current.next
        else:
            prefix_sums[prefix_sum] = current
        
        current = current.next
    
    return dummy.next
# Create the linked list: 3 -> 4 -> -7 -> 5 -> -6 -> 6
head = ListNode(3)
head.next = ListNode(4)
head.next.next = ListNode(-7)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(-6)
head.next.next.next.next.next = ListNode(6)

new_head = delete_zero_sum_sublists(head)

# Print the updated linked list
current = new_head
while current:
    print(current.value, end=" -> ")
    current = current.next    
