"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, new_value):
        new_node = ListNode(new_value)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: 
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, new_value):
        new_node = ListNode(new_value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else: 
            new_node.next = None
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current = self.tail
        if self.head is None and self.tail is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return current.value
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length -= 1
            return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        current = self.head
        #check if empty
        while current:
            if current == node:
                current_prev = current.prev
                current_next = current.next
                if current.next:
                    #current previous points to current next, and vise versa
                    current_prev.next = current_next
                    current_next.prev = current_prev
                    #current head's prev now points to current node
                    self.head.prev = current
                    #current's next now points to head
                    current.next = self.head
                    #head is now current
                    self.head = current
                    #set new head's prev to be None
                    self.head.prev = None
                else:
                    current_prev.next = None
                    current.prev = None
                    current = None
                    self.add_to_head(node.value)
                    self.length -= 1
                    return

            current = current.next      

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node == self.tail:
            return
        else:
            self.add_to_tail(node.value)
            self.delete(node)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current != node:
            current = current.next
        if node == self.head and node == self.tail:
            self.head = None
            self.tail = None
        if current.prev:
            current_prev = current.prev
            current_prev.next = current.next
            if node == self.tail:
                self.tail = current_prev
        if current.next:
            current_next = current.next
            current_next.prev = current.prev
            if node == self.head:
                self.head = current_next
        self.length -= 1

    # def delete(self, node):
    #     self.length -= 1
    #     if not self.head and not self.tail:
    #         return
    #     if self.head == self.tail:
    #         self.head = None
    #         self.tail = None
    #     elif self.head == node:
    #         self.head = node.next
    #         node.delete()
    #     elif self.tail == node:
    #         self.tail = node.prev
    #         node.delete()
    #     else:
    #         node.delete()


    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.value
        # reference to our current node as we traverse the list
        current = self.head.next
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.value > max_value:
                # if so, update our max_value variable
                max_value = current.value
            # update the current node to the next node in the list
            current = current.next
        return max_value

# l = DoublyLinkedList(ListNode(1))
# l.add_to_tail(2)
# l.add_to_tail(3)
# l.add_to_tail(4)
# print("HEAD: ", l.move_to_front(l.tail))