with open('D:/test.txt') as f:
    s = [line for line in f.readline()]
    print(s)

mn = input('Insert ypur name:\n')
with open('D:/test_2.txt', 'w') as f:
    f.write(mn + 'xc  deghtrh')

with open('D:/test_2.txt') as f1:
    print(f1.read())