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


class Deque(Container):

    def left_enqueue(self, item):
        temp = self._container[:]
        self._container = [item] + temp
        return None

    def right_enqueue(self, item):
        self._container.append(item)
        return None

    def left_dequeue(self):
        try:
            item = self._container.pop(0)
        except:
            raise ContainerEmptyException
        return item

    def right_dequeue(self):
        try:
            item = self._container.pop(-1)
        except:
            raise ContainerEmptyException
        return item

class AltQueue(Container):

    def __init__(self):
        Container.__init__(self)
        self._alt = False
        return None

    def push(self, item):
        if not self._alt:
            temp = self._container[:]
            self._container = [item] + temp
            self._alt = not self._alt
        else:
            self._container.append(item)
            self._alt = not self._alt
        return None

    def pop(self):
        try:
            if not self._alt:
                item = self._container.pop(0)
                self._alt = not self._alt
            else:
                item = self._container.pop(-1)
                self._alt = not self._alt
        except:
            raise ContainerEmptyException
        return item

class NeckQueue(Container):

    def pop(self):
        try:
            if len(self._container) >= 2:
                item = self._container.pop(1)
            else:
                item = self._container.pop(0)
        except:
            raise ContainerEmptyException
        return item


class PriorityQueue(Container):

    def __init__(self):
        self._container = {}
        return None

    def push(self, item, priority):
        self._container[priority] = item
        return None

    def pop(self):
        try:
            priorities = self._container.keys()
            maxpriority = min(priorities)
            item = self._container.pop(maxpriority, None)
        except:
            raise ContainerEmptyException
        return item


class Steue(Container):

    def __init__(self):
        Container.__init__(self)
        self._lremove = True
        return None

    def pop(self):
        try:
            if(self._lremove):
                item = self._container.pop(-1)
                self._lremove = not self._lremove
            else:
                item = self._container.pop(0)
                self._lremove = not self._lremove
        except:
            raise ContainerEmptyException
        return item


class SLNode():

    def __init__(self, data=None, next=None):
        self._data = data
        self._next = next
        return None

    def data(self):
        return self._data

    def next(self):
        return self._next

    def set_data(self, data):
        self._data = data
        return None

    def set_next(self, next):
        self._next = next


class DLNode(SLNode):

    def __init__(self, data=None, next=None, prev=None):
        SLLNode.__init__(self, data, next)
        self._prev = prev
        return None

    def prev(self):
        return self._prev

    def set_prev(self, prev):
        self._prev = prev
        return None