from collections.abc import MutableSequence

# Error classes
class IndexOutOfBoundsException(Exception):
    pass

class LinkedNode:
    def __init__(self, value, next_node):
        self.__next = next_node
        self.__value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, next_node):
        self.__next = next_node

class LinkedList(MutableSequence):
    def __init__(self):
        self.__head = None
        self.__len = 0
    
    def __len__(self):
        return self.__len
    
    def __iter__(self):
        next_node = self.__head
        while next_node is not None:
            yield next_node.value
            next_node = next_node.next
    
    def __getitem__(self, index):
        return self.__get(index).value
    
    def __setitem__(self, index, value):
        pass

    def __delitem__(self, index):
        if index == 0:
            self.__head = self.__head.next
        else:
            prev = self.__get(index - 1)
            if index == self.__len - 1:
                prev.next = None
            else:
                prev.next = prev.next.next
        self.__len -= 1
    
    def insert(self, value):
        self.__head = LinkedNode(value, self.__head)
        self.__len += 1

    def __get(self, index):
        if index >= self.__len:
            raise IndexOutOfBoundsException()
        
        next_node = self.__head
        for _ in range(index):
            next_node = next_node.next
        
        return next_node


### Example usage
test_list = LinkedList()

for i in range(10):
    test_list.insert(i)

print(test_list[0])

del test_list[2]

for x in test_list:
    print(x)