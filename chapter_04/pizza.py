# pizza.py

pizzas = ["vegetable", "margherita", "spinach", "barbecue chicken","hawaiian"]

for pie in pizzas:
    print(f"\nI love to eat {pie} pizza with a cold beer!")

print("\nPizza and beer are the best together!\n")

print(f"The first three items of the list are {pizzas[:3]}")

print(f"These are the middle three items of the list: {pizzas[1:-1]}")

print(f"The last three items of the list are {pizzas[-3:]}")

friends_pizzas = pizzas[:]

print(pizzas)
print(friends_pizzas)

pizzas.append("greek")
friends_pizzas.append("pepperoni")

print(pizzas)
print(friends_pizzas)

print(f"My favorite pizzas are {pizzas}.")
print(f"My friend's favorite pizzas are {friends_pizzas}.")

for pizza in pizzas:
    print(f"I love {pizza} pizza!")

for pizza in friends_pizzas:
    print(f"My friend loves {pizza} pizza!")    
