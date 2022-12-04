import array as arr
a = arr.array('i', ['1','2','3'])
for i in range(0, 3):
    print(a[i], end="\n")
print()
print(type(a))
print(a[1])