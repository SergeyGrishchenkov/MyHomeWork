# Write a class Product that has three attributes:
# type
# name
# price
# Then create a class ProductStore, which will have some Products and will operate with all products in the store.
# All methods, in case they can’t perform its action, should raise ValueError with appropriate error information.
# Tips: Use aggregation/composition concepts while implementing the ProductStore class.
# You can also implement additional classes to operate on a certain type of product, etc.
# Also, the ProductStore class must have the following methods:
# add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(30 percent)
# set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by input identifiers (type or name).
# The discount must be specified in percentage
# sell_product(product_name, amount) - removes a particular amount of products from the store if available, in other case raises an error.
# It also increments income if the sell_product method succeeds.
# get_income() - returns amount of many earned by ProductStore instance.
# get_all_products() - returns information about all available products in the store.
# get_product_info(product_name) - returns a tuple with product name and amount of items in the store.

class Product:
    def __init__(self, type: str, name: str, price: float):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    __price_premium = 30
    __income = 0
    __disc_message = "The discount has been set for:"

    def __init__(self, address: str, products: object = []):
        self.address = address
        self.products = products

    def add(self, product: Product, amount: float):
        try:
            if amount <= 0:
                raise ValueError
            product.price *= ((self.__price_premium / 100) + 1)
            product.amount = amount
            self.products.append(product)
        except ValueError:
            print("Impossible to add product with amount < 0!")

    def set_discount(self, identifier, percent, identifier_type=''):
        try:
            counter = 0
            for item in self.products:
                if item.name == identifier or item.type == identifier_type:
                    item.discount = percent
                    counter += 1
                    print(f"{self.__disc_message} {item.name}")
            if counter == 0:
                raise ValueError
        except ValueError:
            print(f'Impossible to set discount for product: {identifier} or type: {identifier_type}')

    def sell_product(self, product_name, amount):
        try:
            if amount <= 0:
                raise ValueError
            for item in self.products:
                if item.name == product_name and item.amount >= amount:
                    if amount > item.amount:
                        raise ValueError
                    print(f'Going to sell - {item.name}, Now we have - {item.amount}')
                    item.amount -= amount
                    self.__income += amount * (item.price if not 'discount' in item.__dict__ else item.price * (1 - item.discount / 100) )
                    print(f'{item.name} sold in quantity - {amount}, on the balance - {item.amount}')
        except ValueError:
            print("Impossible to sell with such amount !!!")

    def get_income(self):
        return self.__income

    def get_product_info(self, product_name: str):
        return tuple((x.__dict__['name'], x.__dict__['amount']) for x in self.products if x.__dict__['name'] == product_name)[0]

    def get_all_products(self):
        return tuple((x.__dict__['name'], x.__dict__['amount']) for x in self.products)


p = Product('Sport', 'Football T-Shirt', 100)

p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore('dgshj')

s.add(p, 10)

s.add(p2, 300)

s.sell_product('Ramen', 10)
print(s.get_all_products())
print(f'The total income is: {s.get_income()}')
print(s.get_product_info('Ramen'))
assert s.get_product_info('Ramen') == ('Ramen', 290)

s.set_discount('Football T-Shirt', 20)
print(s.products[0].__dict__)
s.sell_product('Football T-Shirt', 2)
print(f'The total income is: {s.get_income()}')
print(s.products[0].__dict__)


