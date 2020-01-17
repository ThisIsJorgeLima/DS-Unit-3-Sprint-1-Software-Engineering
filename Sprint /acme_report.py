import unittest
import random
import math
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    
    """
    Part 4 - Class Report
    Function to create # of Obj. from product Class.
    It will generate a given number of products (default 30),
    randomly, and return them as a list inventory_report
    """
    products = []
    adj_sample = random.sample(ADJECTIVES)
    nouns_sample = random.sample(NOUNS, 1)
    name = f'{adjectives_sample} {nouns_sample}'

    price = random.randint(5, 100)
    weight = random.radint(5, 100)
    flammability = random.uniform(0.0, 2.5)

prod = Product(name=name,weight=weight,flammability=flammability)

list_of_products = [prod.name, prod.price, prod.weight, prod.flammability]

products.append(list_of_products * num_products)

return list_of_products

def inventory_report(products):
  """
  inventory_report will take a list of products, and prints a "nice" summary
  """

for name in products:
  count = []
  if name not in count:
    count.append(name)
  num_of_unique_prod = len(count)
return num_of_unique_prod

unique_prod = num_of_unique_prod
avg_price = sum(products.price)/len(products.price)
avg_weight = sum(products.weight)/len(products.weight)
avg_flammability = sum(products.flammability)/len(products.flammability)

print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
print(f'Uniqute product names: {unique_prod}')
print(f'Average Price: {avg_price}')
print(f'Avergae Weight: {avg_weight}')
print(f'Average Flammability: {avg_flammability}')

if __name__ == '__main__':
    inventory_report(generate_products())