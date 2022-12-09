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

    def __init__(self, address: str, products: object = []):
        self.address = address
        self.products = products

    def add(self, product: Product, amount: float):
        try:
            product.price *= ((self.__price_premium / 100) + 1)
            product.amount = amount
            self.products.append(product)
        except:
            raise ValueError("Impossible to add priduct!")

    def set_discount(self, identifier, percent, identifier_type=''):
        try:
            list(filter(lambda y: y['type'] == 'Food', [x.__dict__ for x in self.products]))
        except:
            raise ValueError("Impossible to set discount!")

    def sell_product(self, product_name, amount):
        try:
            for item in self.products:
                if item.name == product_name and item.amount >= amount:
                    before_sell = self.get_product_info(product_name)
                    print(f'Going to sell - {item.name}, Now we have - {item.amount}')
                    item.amount -= amount
                    self.__income += amount * item.price
                    after_sell = self.get_product_info(product_name)
                    print(f'{item.name} sold in quantity - {amount}, on the balance - {item.amount}')
        except:
            raise ValueError("Impossible to sell!!")

    def get_income(self):
        try:
            return self.__income
        except:
            raise ValueError("Impossible to get income!")

    def get_product_info(self, product_name: str):
        try:
            return tuple((x.__dict__['name'], x.__dict__['amount']) for x in self.products if x.__dict__['name'] == product_name)[0]
        except:
            raise ValueError("There are not such product!!")

    def get_all_products(self):
        try:
            return tuple((x.__dict__['name'], x.__dict__['amount']) for x in self.products)
        except:
            raise ValueError("Impossible to show information!!")


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
# for item in stor.products:
#     print(type(item))
#     if 'Food' in item.__dict__.values():
#         print(item.__dict__)
#
# list_a = [-2, -1, 0, 1, 2, 3, 4, 5]    # Пусть у нас есть исходный список
# list_b = [x.__dict__ for x in stor.products]
# #def test(d):
#
# lll = list(filter(lambda y: y['type'] == 'Food', [x.__dict__ for x in stor.products]))
#
# ll = [x.__dict__ for x in stor.products]
# print(ll)
# #ww = tuple(filter(lambda y: y['name'] == 'Ramen', (x.__dict__ for x in stor.products)))
# ww = tuple((x.__dict__['name'], x.__dict__['amount']) for x in stor.products if x.__dict__['name'] == 'Ramen')[0]
# print(ww)
#
# s.add(p2, 300)
#
# s.sell(‘Ramen’, 10)
#
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

