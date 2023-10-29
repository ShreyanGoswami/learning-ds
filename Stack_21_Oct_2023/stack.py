class Stack:
    def __init__(self, MAX_SIZE):
        pass

    def push(self, x):
        pass

    def peek(self):
        pass

    def pop(self):
        pass

    def clear(self):
        pass

    def in_order_stack(self):
        pass

def _init_stack():
    s = Stack(3)
    s.push(1)
    s.push(2)
    s.push(3)
    return s

def test():
    print(f'Running basic test')
    s = _init_stack()

    assert s.peek() == 3

    x = s.pop()

    assert x == 3
    assert s.peek() == 2
    print(f'Passed basic test')

def test_in_order():
    print(f'Testing in order stack') 
    s = _init_stack()
    in_order_stack = s.in_order_stack()

    assert in_order_stack.peek() == 1
    in_order_stack.pop()

    assert in_order_stack.peek() == 2
    in_order_stack.pop()

    assert in_order_stack.peek() == 3
    in_order_stack.pop()

    print(f'Passed in order stack') 

if __name__ == '__main__':
    test()
    test_in_order()