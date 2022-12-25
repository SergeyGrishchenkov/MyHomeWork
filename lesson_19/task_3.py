# Create your own implementation of an iterable, which could be used inside for-in loop.
# Also, add logic for retrieving elements using square brackets syntax.

import itertools
class MyIter:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            self.start += 1
            return self.start

my = MyIter(1,5)
for i in my:
    print(i)