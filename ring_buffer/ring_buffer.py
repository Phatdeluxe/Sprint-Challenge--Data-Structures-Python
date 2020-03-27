from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # if empty
        if len(self.storage) == 0:
            # add to tail
            self.storage.add_to_tail(item)
            # set current to node
            self.current = self.storage.tail

        # if not full add item to tail
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)

        # if full
        else:
        # if current is tail
            if self.current == self.storage.tail:
                # replace current with new value
                self.storage.tail.value = item
                # change current to head
                self.current = self.storage.head
            else:
                # replace current with new value
                self.current.value = item
                # change current to current.next
                self.current = self.current.next

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        node = self.storage.head
        list_buffer_contents.append(node.value)
        while node.next:
            node = node.next
            list_buffer_contents.append(node.value)

        return list_buffer_contents


# test = RingBuffer(5)
# test.append('b')
# test.append('a')
# test.append('c')
# test.append('d')
# print(test.get())



# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity 
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        return_list = []
        for i in self.storage:
            if i != None:
                return_list.append(i)
        return return_list
