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


if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_begining(5)
    # ll.insert_begining(89)
    # ll.insert_end(5)
    # ll.insert_end(5)
    ll.insert_list([2, 5, 3, 9, 0, 7])
    ll.print()
