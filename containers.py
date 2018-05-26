class ContainerEmptyException(Exception):
    def __str__(self):
        return "The container you are trying to pop from is empty"

class ContainerFullException(Exception):
    def __str__(self):
        return "The container you are trying to push into is full"


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


class Queue(Container):

    def pop(self):
        try:
            item = self._container.pop(0)
        except:
            raise ContainerEmptyException
        return item

class Bucket(Container):

    def push(self, item):
        if len(self._container) == 1:
            raise ContainerFullException
        else:
            self._container = [item]

    def pop(self):
        try:
            item = self._container.pop(0)
        except:
            raise ContainerEmptyException
        return item