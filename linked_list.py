from collections.abc import MutableSequence

# Error classes
class IndexOutOfBoundsException(Exception):
    pass

class LinkedNode:
    def __init__(self, value, next_node):
        self.__next = next_node
        self.__value = value
    
    def value():
        return self.__value
    
    def next():
        return self.__next

class LinkedList(MutableSequence):
    def __init__(self):
        self.__head = None
        self.__len = 0
    
    def __len__(self):
        return self.__len
    
    def __iter__(self):
        next_node = self.head
        while next_node is not None:
            yield next_node.value()
            next_node = next_node.next()
    
    def __getitem__(self, index):
        pass
    
    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        pass
    
    def insert(self, value):
        self.__head = LinkedNode(value, self.__head)

    def __get(self, index):
        if index >= self.len:
            raise IndexOutOfBoundsException()
        
        next_node = self.head
        for _ in 0..index:
            next_node = next_node.next()
        
        return next_node

test_list = LinkedList()

for i in 0..10:
    test_list.insert(i)

print test_list[0]

for x in test_list:
    print x