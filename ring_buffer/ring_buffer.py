from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if the length of DLL is less than capacity (to signify there is space avail)
        if len(self.storage) < self.capacity:
            # add node with the item value to the tail of the DLL
            self.storage.add_to_tail(item)
        # if current is None
        elif self.current is None:
            # set current to the head
            self.current = self.storage.head
            # assign item to current value
            self.current.value = item
            # set current to the next node
            self.current = self.current.next
        else:
            # assign the item to the current value
            self.current.value = item
            # set current to the next node
            self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # set a variable to iterate through the DLL
        current_node = self.storage.head
        # iterate through the DLL
        while current_node is not None:
            # append the DLL values to list
            list_buffer_contents.append(current_node.value)
            # set current_node to next node
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
