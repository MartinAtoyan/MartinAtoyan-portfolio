def item_cost_with_tax(item_cost, tax = 0.05): 
    return item_cost * (1 + tax)

item_cost = 50
print(item_cost_with_tax(item_cost))
