from random import randint, sample, uniform
import numpy as np
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS      = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']

def generate_products(iterator):
    
    product_list = []
    
    while iterator != 0:
        name         = sample(ADJECTIVES, 1)[0] + ' ' + sample(NOUNS, 1)[0]
        price        = randint(5, 100) # 5 to 100
        weight       = randint(5, 100) # 5 to 100
        flammability = uniform(0.0, 2.5) # 0.0 to 2.5
        
        product_info = [name
                       ,price
                       ,weight
                       ,flammability
                       ]

        product_list.append(product_info)
        iterator    -= 1
        
    return product_list



def inventory_report(product_list):
    # Unique product names
    # avg price, weight, flam
    
    iterator = len(product_list)
    
    names          = []
    prices         = []
    weights        = []
    flammabilities = []
    
    for product in product_list:
        names.append(product[0])
        prices.append(product[1])
        weights.append(product[2])
        flammabilities.append(product[3])
        
    report = [('Unique names: \t\t\t%s'       % set(names))
             ,('Prices average: \t\t%d'       % np.mean(prices))
             ,('Weights average: \t\t%d'      % np.mean(weights))
             ,('Flammabilities average: \t%d' % np.mean(flammabilities))
             ]
    
    return report, names, prices, weights, flammabilities


if __name__ == '__main__':
    inventory_report(generate_products())