#Input data:

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
sum = 0
for k, value in stock.items():
    sum += value * prices[k]
print(f'The total price of the stock is: {sum}')