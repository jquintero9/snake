
class Stack(object):

    """
    This class simulates behavior a stack.
    """
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.is_empty():
            self.__items.pop()

    def peek(self):
        try:
            return self.__items[-1]
        except IndexError:
            return None

    def size(self):
        return len(self.__items)

    def __repr__(self):
        return self.__items.__str__()

