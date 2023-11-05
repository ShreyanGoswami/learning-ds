"""
A monotonically increasing stack always maintains a increasing order of elements

When the stack is empty add element to the stack
In case there are elements in the stack and the element at the top of the stack is greater than the element to be added, keep removing elements from the stack until:
    1) The stack is empty
    2) The top element of the stack is less than the new element to be added

Implement a monotonically increasing stack.
The push function should behave according to the above logic
The pop and peek functions should behave as they normally do in a normal stack
The inspectStack function is a purely helper function that returns a list of elements in the stack bottom up
"""

class MonotonicIncreasingStack:


    def __init__(self):
        self.s = [] # use this list for implementing the monotonic stack

    def push(self, x):
        if len(self.s) == 0:
            self.s.append(x)
        else:
            while self.peek() > x:
                if len(self.s) == 0 or self.peek() < x:
                    break
                self.pop()

            self.s.append(x)
        
    def peek(self):
        if self.s:
            return self.s[-1]
        return float('-inf')

    def pop(self):
        return self.s.pop()
    
    def inspectStack(self):
        return self.s

def test():
    s = MonotonicIncreasingStack()

    assert s.inspectStack() == []

    data = [1, 2, 3, 3]
    for x in data:
        s.push(x)

    assert s.inspectStack() == data

    s.push(5)
    assert [1, 2, 3, 3, 5] == s.inspectStack()

    s.push(4)
    assert [1, 2, 3, 3, 4] == s.inspectStack()

    s.push(2)
    assert [1, 2] == s.inspectStack()

    s.push(0)
    assert [0] == s.inspectStack()

if __name__ == "__main__":
    test()
