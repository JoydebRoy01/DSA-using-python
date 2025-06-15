# Node class
class Node:
    def __init__(self, data):
        self.data = data  # Store data
        self.next = None  # Pointer to next node

# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Traverse and print the list
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Search for a value in the list
    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    # Insert a new node at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Delete a node by value
    def delete_node(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            current = None
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Element {key} not found!")
            return

        prev.next = current.next
        current = None

# Test the LinkedList
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_beginning(5)

print("Linked List after insertion:")
ll.traverse()

print("Searching for 20:", ll.search(20))
print("Searching for 99:", ll.search(99))

ll.delete_node(20)
print("Linked List after deleting 20:")
ll.traverse()

ll.delete_node(100) 
