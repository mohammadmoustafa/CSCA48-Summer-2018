class EmptyContainerError(Exception):
    def __str__(self):
        return "The container you are trying to pop from is empty"


class Container():

    def __init__(self):
        self._container = []
        return None

    def push(self, item):
        self._container.append(item)
        return None

    def is_empty(self):
        return self._container == [] or self._container == {}


class Stack(Container):

    def pop(self):
        try:
            item = self._container.pop(-1)
        except:
            raise EmptyContainerError
        return item