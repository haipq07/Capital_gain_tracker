class LinkedDeque:
    class DLNode:
        def __init__(self, previous_node=None, data_portion=None, next_node=None):
            self.previous_node = previous_node
            self.data_portion = data_portion
            self.next_node = next_node

        def get_data(self):
            return self.data_portion

        def set_data(self, new_data):
            self.data_portion = new_data

        def get_next_node(self):
            return self.next_node

        def set_next_node(self, next_node):
            self.next_node = next_node

        def get_previous_node(self):
            return self.previous_node

        def set_previous_node(self, previous_node):
            self.previous_node = previous_node

    def __init__(self):
        self.front = None
        self.back = None
# Add an entry to the back of the deque
    def add_to_back(self, new_entry):
        new_node = self.DLNode(data_portion=new_entry)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.set_previous_node(self.back)
            self.back.set_next_node(new_node)
            self.back = new_node
 # Add an entry to the front of the deque
    def add_to_front(self, new_entry):
        new_node = self.DLNode(data_portion=new_entry)
        if self.is_empty():
            self.front = new_node
            self.back = new_node
        else:
            new_node.set_next_node(self.front)
            self.front.set_previous_node(new_node)
            self.front = new_node
# Get the data from the back of the deque
    def get_back(self):
        if self.is_empty():
            return None
        return self.back.get_data()
# Get the data from the front of the deque
    def get_front(self):
        if self.is_empty():
            return None
        return self.front.get_data()
# Remove and return the entry at the front of the deque
    def remove_front(self):
        if self.is_empty():
            return None
        removed_data = self.front.get_data()
        self.front = self.front.get_next_node()
        if self.front is not None:
            self.front.set_previous_node(None)
        else:
            self.back = None
        return removed_data
# Remove and return the entry at the back of the deque
    def remove_back(self):
        if self.is_empty():
            return None
        removed_data = self.back.get_data()
        self.back = self.back.get_previous_node()
        if self.back is not None:
            self.back.set_next_node(None)
        else:
            self.front = None
        return removed_data

    def clear(self):
        self.front = None
        self.back = None

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        while current is not None:
            print(current.get_data(), end=" -> ")
            current = current.get_next_node()
        print("None")
