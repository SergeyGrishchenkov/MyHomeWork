# Create your own implementation of a built-in function range,
# named in_range(), which takes three parameters: `start`, `end`,
# and optional step. Tips: See the documentation for `range` function

def in_range(start, end, step=1):
    if isinstance(start, int) and isinstance(end, int) and isinstance(step, int) and step != 0:
        while start < end if step > 0 else start > end:
            yield start
            start += step
    else:
        raise TypeError


print(f'{"*" * 10} ORIGINAL FUNCTION {"*" * 10}')
for i in range(-2, 7, 2):
    print(i)
print(f'{"*" * 10} my_'
      f' generotop {"*" * 10}')
for i in in_range(-2, 7, 2):
    print(i)


print(f'{"*" * 10} ORIGINAL FUNCTION {"*" * 10}')
for i in range(9, 1, -2):
    print(i)
print(f'{"*" * 10} my_'
      f' generotop {"*" * 10}')
for i in in_range(9, 1, -2):
    print(i)
