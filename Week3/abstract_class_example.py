from abc import ABC, abstractmethod

class OperatingSystem(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def mymethod(self):
        pass

    def mymethod2(self):
        return "I am an operating system. This method can be overriden" +\
               " but has a default implementation."


class Windows(OperatingSystem):

    def mymethod(self):
        return "I am a Windows Operating System"


class Mac(OperatingSystem):

    def mymethod(self):
        return "I am a Mac Operating System"


class Linux(OperatingSystem):

    def mymethod(self):
        return "I am a Linux Operating System"


if __name__ == "__main__":
    # change this variable so that it is either Linux(), Mac(), or Windows()
    os = Windows()
    # since they are all from the same abstract class, we don't need to
    # change any of this code
    print(os.mymethod())
    print(os.mymethod2())