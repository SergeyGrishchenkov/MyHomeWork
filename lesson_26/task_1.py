from collections import deque

test_string = "My string to work with stack!!"
rev_test_str = ""

stack = deque()
for item in test_string:
    stack.append(item)

while len(stack) > 0:
    rev_test_str += stack.pop()

print(rev_test_str)