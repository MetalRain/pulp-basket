from pulp import *

def batch_discount():
    '''
    Batch discount

    one litre of milk costs 0.89€
    if you buy three pieces of milk they get discounted 10%

    What is the price of 7 litres of milk?

    two variables:
    singles
    batches

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

    print("singles:", x_s.value())
    print("batches:", x_b.value())
    print("basket price:", model.objective.value())

if __name__ == '__main__':
    batch_discount()