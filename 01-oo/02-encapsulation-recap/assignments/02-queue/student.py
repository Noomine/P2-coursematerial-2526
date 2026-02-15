class Queue: 
    def __init__(self):
        self.__items = []

    def is_empty(self):
        if len(self.__items) == 0:
            return True 
        
    def add(self, item):
        self.__items.append(item)
    
    def next(self):
        value = self.__items.pop(0)
        return value

# queue = Queue()


# queue.add('a')
# queue.add('b')
# queue.add('c')

# print(queue.get_items())