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

    def __init__(self, address: str, income: int = 0, products: object = []):
        self.address = address
        self.income = income
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
            pass
        except:
            raise ValueError("Impossible to set discount!")

    def sell_product(self, product_name, amount):
        try:
            pass
        except:
            raise ValueError("Impossible to set discount!")

    def get_income(self):
        try:
            pass
        except:
            raise ValueError("Impossible to set discount!")

    def get_product_info(self, product_name):
        try:
            pass
        except:
            raise ValueError("Impossible to set discount!")

    def get_all_products(self):
        try:
            pass
        except:
            raise ValueError("Impossible to set discount!")


p = Product('Sport', 'Football T-Shirt', 100)
#
p2 = Product('Food', 'Ramen', 1.5)
#
stor = ProductStore('sadghj')
#
stor.add(p, 10)
stor.add(p2, 220)
aa = stor.products.copy()
for item in stor.products:
    print(type(item))
    if 'Food' in item.__dict__.values():
        print(item.__dict__)

list_a = [-2, -1, 0, 1, 2, 3, 4, 5]    # Пусть у нас есть исходный список
list_b = [x.__dict__ for x in stor.products]
print(list_b)
#
# s.add(p2, 300)
#
# s.sell(‘Ramen’, 10)
#
# assert s.get_product_info(‘Ramen’) == (‘Ramen’, 290)

