from containers import *

def decimal_to_binary(decimalNum):
    '''(int) -> str
    Returns the binary representation of the given decimal number as a string.
    REQ: <decimalNum> >= 0
    '''
    # declare the stack we are going to use, as well as our result variable
    stack = Stack()
    result = ""

    # check if the number given is a zero, set result to zero
    if decimalNum == 0: result = "0"

    # while our number is greater than zero, we repeat the steps
    while decimalNum > 0:
        # get the remainder of the integer division
        remainder = decimalNum % 2
        # push the remainder into the stack
        stack.push(remainder)
        # (integer) divide our number by 2, and repeat the process
        decimalNum = decimalNum // 2

    # while we have items still in our stack
    while not stack.is_empty():
        # pop the items out and add them to our result string
        result += str(stack.pop())

    return result

if __name__ == "__main__":

    print("4 => " + decimal_to_binary(4))
    print("27 => " + decimal_to_binary(27))