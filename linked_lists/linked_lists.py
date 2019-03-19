"""Practice implementations of Singlylinked and Doublylinked lists."""


class NodeLinked:
    """Node object for singly linked lists.

    Each node contains a key value and a pointe to to a next node.
    """

    def __init__(self, value):
        """Initialize the Node witha value."""
        self.value = value
        self.next = None

    def set_next(self, node):
        """Set the next pointer."""
        self.next = node

    def set_next_to_none(self):
        """Set the next point to None."""
        self.next = None

    def __repr__(self):
        """Set print format."""
        s = "value: {}\n".format(self.value)
        if self.next is not None:
            s += "next: {}".format(self.next.value)
            return s
        else:
            s += "next: None"
            return s


class NodeDoublyLinked(NodeLinked):
    """Node object for adoubly linked list.

    Defined as a inherited class for practice.
    """

    def __init__(self, value):
        """Initialize th node."""
        super(NodeDoublyLinked, self).__init__(value)
        self.previous = None

    def set_previous(self, node):
        """Set the value for pointer to previous node."""
        self.previous = node

    def set_previous_to_null(self, node):
        """Set teh 'previous' pointer to None."""
        self.previous = None

    def __repr__(self):
        """Print preresentation."""
        s = super(NodeDoublyLinked, self).__repr__()

        if self.previous is not None:
            s += "\nprevious: {}".format(self.previous.value)
            return s
        else:
            s += "\nprevious: None"
            return s


class SinglyLinkedList():
    """Singly Linked List data structure with end pointer."""

    def __init__(self):
        """Initialize the linked list."""
        self._head = None
        self._tail = None

    def push_front(self, value):
        """Add a node containg value the front of the list.
        """
        # if list is empty, simply initialize the node
        if self.is_empty():
            # check if the linked list has no nodes
            self._head = NodeLinked(value)
            self._tail = self._head

        # if list isn't empty, update
        else:
            old = self._head
            self._head = NodeLinked(value)
            self._head.next = old

    def top_front(self):
        """Return the value node from the front of the list without
           removing it.
        """
        if not self.is_empty():
            return self._head.value
        else:
            return None

    def pop_front(self):
        """Return the node from the front of the list and
           remove that node from the list.
        """
        if not self.is_empty():
            popped = self._head
            self._head = popped.next
            return popped.value
        else:
            return None

    def push_back(self, value):
        """Add an node containing value to the back of the list."""
        if self.is_empty():
            self._head = NodeLinked(value)
            self._tail = self._head
        else:
            old_tail = self._tail
            self._tail = NodeLinked(value)
            old_tail.next = self._tail

    def top_back(self):
        """Return the value in the node at the back of the list without
           removing the node.
        """
        if not self.is_empty():
            self._tail.value
        else:
            return None

    def pop_back(self):
        """Return the value of the node at the back of the list and
           remove that node from the list.
        """
        if self.is_empty():
            return None
        elif self._head == self._tail:
            val = self._head.value
            self._head = None
            self._tail = None
            return val

        old_tail = self._tail
        next_to_last = self._find_prev(old_tail)
        next_to_last.next = None
        self._tail = next_to_last
        return old_tail.value

    def find(self, key):
        """Return True if the key is in the list, False otherwise."""
        # return false if the list is empty
        if self.is_empty():
            return False

        # loop through nodes and return true if key is found
        current_node = self._head
        while current_node is not None:
            if current_node.value == key:
                return True
            else:
                current_node = current_node.next
        return False

    def erase(self, key):
        """Remove a node containing the key value from the list."""
        if self.is_empty():
            return None

        if self._head.value == key:
            self._head = self._head.next

        else:
            prev, current = self._traverse_to_value(key)
            if current is not None:
                prev.next = current.next
                if prev.next is None:
                    self._tail = prev
        return None

    def is_empty(self):
        """Return True if list is empty, false otherwise.
        """
        return self._head is None

    def add_before(self, target, value):
        """Add a node before a key and do nothing if value is not in the list.
        """
        if self.is_empty():
            return
        elif self._head.value == target:
            self.push_front(value)
        else:
            prev, _next = self._traverse_to_value(target)
            if _next is not None:
                current = NodeLinked(value)
                current.next = _next
                prev.next = current

    def add_after(self, target, value):
        """Add a node to before a target value."""
        if self.is_empty():
            return

        if self._tail.value == target:
            self.push_back(value)
        else:
            prevprev, prev = self._traverse_to_value(target)
            if prev is not None:
                current = NodeLinked(value)
                current.next = prev.next
                prev.next = current

    def reverse_in_place(self):
        """Reverse order of values in list in place.

        Do not copy or duplicate any nodes.
        """
        # if empty list return
        if self.is_empty():
            return None

        # if this is a single element list, return
        if self._tail == self._head:
            return None

        # if this is a multi-element list loop
        else:
            # redirect tail pointer
            self._tail = self._head

            # reverse pointers in head node
            current = self._head
            _next = current.next
            current.next = None

            # loop through nodes reversing the pointers
            while _next is not None:

                # increment the node and reverse pointers
                prev = current
                current = _next
                _next = current.next
                current.next = prev

            self._head = current
        return None

    def _traverse_to_node(self, target):
        """Return the node in the linked list and it's prior node."""
        # loop through the list for the
        # node pointing to node
        prev = None
        current = self._head
        while current != target:
            prev = current
            current = prev.next
            if prev.next is None:
                return None, None

        return prev, current

    def _traverse_to_value(self, value):
        """Find the node in the linked list.

        Takes: a head pointer to non-empty linked list
        Returns: prev, current nodes if an element is found.
                 None, None if element is not found
        """
        prev = None
        current = self._head

        # loop until you reach a node with a matching value
        while current.value != value:
            if current.next is None:
                return None, None

            prev = current
            current = current.next

        # return that node and hte previous node
        return prev, current

    def _find_prev(self, node):
        """Find the node in the linked list prior to node.

        Requires that self is not empty and that node is not the head node.
        """
        # loop throuhgh the list for the
        # node pointing to node
        current = self._head
        _next = current.next
        while current.next != node:
            _next = current.next
            current = _next
        return current
