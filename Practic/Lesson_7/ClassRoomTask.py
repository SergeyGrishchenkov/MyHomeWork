#list compre
str_c = [1, 3, 2, 5, 6]

i = 0
while i < len(str_c):

# for i in range(len(str_c)):
    if str_c[i] % 3 == 0:
        i += 1
        continue
    str_c[i] *= 5
    i += 1
else:
    print('JR')
print(str_c)