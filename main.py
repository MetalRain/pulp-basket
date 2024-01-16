from pulp import *
from dataclasses import dataclass
from typing import Optional

def batch_discount():
    '''
    Batch discount

    one litre of milk costs 0.89€
    if you buy three pieces of milk they get discounted 10%

    What is the price of 7 litres of milk?

    two variables:
    - singles
    - batches

    constraints:
    singles * 1 + batches * 3 = 7

    minimize:
    singles * 0.89 + batches * 3 * 0.89 * 0.9


    '''
    model = LpProblem(sense=LpMinimize)

    # variables
    x_s = LpVariable(name="singles", lowBound=0, cat='Integer')
    x_b = LpVariable(name="batches", lowBound=0, cat='Integer')

    # constraints 
    model += x_s + x_b * 3 >= 7
    model += x_s + x_b * 3 <= 7

    # objective function
    model += x_s * 0.89 + x_b * 3 * 0.89 * 0.9

    # solve (ignoring debug messages)
    status = model.solve(PULP_CBC_CMD(msg=False))


    print("single milks:", x_s.value())
    print("milk batches:", x_b.value())
    print("basket price:", model.objective.value())
    print("expected price:", 0.89 + 2 * 3 * 0.89 * 0.9)


def dynamic():
    '''
    Can you dynamically build ILP problem
    just using pricing rules?
    '''

    # Pricing rule 1:
    # if total is greater than 50€, delivery is free

    # Pricing rule 2:
    # if you buy three items from selection A (which contains multiple products), each gets 5% discount

    # Pricing rule 3:
    # if product has manual discount (for example old model), you get it 30% off

    # Assume basket contains items that do match to above rules and then "normal" items.
    # Can you assign variables with algorithm?

    @dataclass
    class Product:
        name: str
        amount: int
        normal_price: float
        selection: Optional[int]
        manual_discount: bool

    products = [
        Product("milk", 2, 0.89, None, False),
        Product("coffee maker", 1, 39.90, None, True),
        Product("dark roast coffee", 1, 6.95, 1, False),
        Product("medium roast coffee", 1, 5.55, 1, False),
        Product("light roast coffee", 1, 5.95, 1, False),
        Product("delivery", 1, 11.95, None, False),
    ]

    # Variable choosing algorithm

    # Rule 1
    # variables don't know the total sum, maybe calculate this after ILP

    # Rule 2
    # 1. Find items belonging to selections, similar to batch discount example
    #    each item has non discounted variable and one belonging to discount.
    #
    #    What if you have 4 items that can be included in the discount, but some are more expensive
    #    maybe sort by price such that highest price items are more likely used in discount instead
    #    of leaving as singles. 🤔

    # Rule 3
    # Split products to "two", one with discount and one without

if __name__ == '__main__':
    batch_discount()