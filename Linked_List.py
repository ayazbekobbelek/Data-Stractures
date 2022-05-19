class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    # Initialize linked list
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # Iteration through linked list (for i in linked list)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    # Representation of linked list (used for to print the linked list easier)
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return " -> ".join(nodes)

    # Adding node to the beginning of linked list
    def add_first(self, node):
        node.next = self.head
        self.head = node

    # Add node ot the end of linked list
    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    # Inserting between two nodes - can be done after or before certain node
    # Inserting after
    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("The list is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception(f"Node with data {target_node_data} not found")

    # Inserting before
    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("The list is empty")
        if target_node_data == self.head.data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception(f"Node with data {target_node_data} not found")

    # Removing a Node
    def remove_node(self, target_data_node):
        if self.head is None:
            raise Exception("The list is empty")
        if self.head.data == target_data_node:
            self.head = self.head.next
            return
        prev_node = self.head
        for node in self:
            if node.data == target_data_node:
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception(f"Node with data {target_data_node} not found")

    # Reverse a linked list
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


llist = LinkedList(nodes=['a', 'b', 'c'])
llist.add_first(Node("d"))
llist.add_last(Node('e'))
llist.add_after("b", Node("f"))
llist.add_before("c", Node("g"))
llist.remove_node("c")

llist2 = LinkedList(nodes=['a', 'b', 'c'])
llist2.reverse()
print(llist2)
