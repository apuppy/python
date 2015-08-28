shopping_list = ["banana", "orange", "apple"]

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

# Write your code below!
def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            stock[i] -= 1
            total += prices[i]
    return total

cost = compute_bill(shopping_list)
print(cost)