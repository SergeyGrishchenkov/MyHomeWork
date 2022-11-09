x = 10
for i in [1,2,3,4,5]:
    if i % 2 == 0:
        break
    x -= i
else:
    x = 10
print(x)