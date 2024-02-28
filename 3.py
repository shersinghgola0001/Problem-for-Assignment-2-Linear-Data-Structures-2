#Q3. Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def merge_alternate(head1, head2):
    if not head1:
        return head2
    if not head2:
        return head1
    
    current1 = head1
    current2 = head2
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        
        current1.next = current2
        current2.next = next1
        
        current1 = next1
        current2 = next2
    
    return head1 
head1 = Node(1)
head1.next = Node(3)
head1.next.next = Node(5)
head1.next.next.next = Node(7)

head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)

merged_head = merge_alternate(head1, head2)

current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
