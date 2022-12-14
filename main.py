class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linkedlist is empty')
            return
        else:
            node = self.head
            llstr = ''
            while node:
                llstr += str(node.data) + ' --> '
                node = node.next
            print(llstr)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data, None)

    def insert_list(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_end(data)

    def get_length(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def remove_node(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index.')
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node.next = node.next.next
                break
            node = node.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        if index == 0:
            self.insert_begining(data)
            return
        count = 0
        node = self.head
        while node:
            if count == index - 1:
                node = Node(data, node.next)
                node.next = node
                break
            node = node.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_begining(5)
    # ll.insert_begining(89)
    # ll.insert_end(5)
    # ll.insert_end(5)
    ll.insert_list([2, 5, 3, 9, 0, 7])
    ll.print()
    print(ll.get_length())
    ll.remove_node(2)
    ll.print()
    ll.insert_at(0, 2)
    ll.print()
