class InvalidIndexError(Exception):
    pass

class InvalidAdditionError(Exception):
    pass

class Vector:

    def __init__(self, size):
        '''(Vector, int) -> NoneType
        Instantiate a vector of size <size>.
        '''
        # initialize the class variables
        self._size = size
        # vector defaults to a zero vector
        self._vector = [0] * size

    def __eq__(self, other):
        '''(Vector, Vector) -> bool
        Returns True if this vector is equivalent to the <other> vector.
        '''
        return self._vector == other._vector

    def __str__(self):
        '''(Vector) -> str
        Returns the string version of the vector.
        '''
        return str(self._vector)

    def length(self):
        '''(Vector) -> int
        Returns the length of the vector.
        '''
        return self._size

    def get(self, i):
        '''(Vector, int) -> obj
        Returns the item found at index <i> in the vector.
        '''
        # Check to make sure that the index is within range,
        # otherwise throw an error
        if i >= self._size:
            raise InvalidIndexError("The given index is larger than the size" +
                                    " of the vector")
        return self._vector[i]

    def set(self, i, item):
        '''(Vector, int, obj) -> NoneType
        Set the item at index <i> in the vector to <item>
        '''
        # Check to make sure that the index is within range,
        # otherwise throw an error
        if i >= self._size:
            raise InvalidIndexError("The given index is larger than the size" +
                                    " of the vector")
        self._vector[i] = item

    def add(self, vector):
        '''(Vector, Vector) -> Vector
        Returns a vector that is the result of adding this vector with the
        given vector.
        REQ: <vector> must be the same size as me
        '''
        # If the two vectors are not the same size, throw an error and exit
        if self._size != vector._size:
            raise InvalidAdditionError("The two vectors must be of the same" +
                                       " size")

        # Create a resultant vector to store the result of adding the two
        # vectors
        resultant = Vector(self._size)
        # For each item in the vector, add it with the corresponding item
        # in the other vector and set it in the result vector
        for i in range(self._size):
            resultant.set(i, (self.get(i) + vector.get(i)))
        return resultant


if __name__ == "__main__":
    a = Vector(2)
    b = Vector(2)
    c = Vector(3)

    print(a.length())
    print(b.length())
    print(c.length())

    print(a.get(0))

    print(a)
    print(b)
    print(a == b)

    print(a.set(0, 2))
    print(a.get(0))

    #print(a.get(2))
    print(a.add(b))
    #print(a.add(c))
