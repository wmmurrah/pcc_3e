# foods_tuple.py

foods = ("sushi", "salad", "soup", "tacos", "pasta")

for food in foods:
    print(food)

foods[1] = "grain bowl"

foods = ("sushi", "grain bowl", "soup", "tacos", "pasta")

for food in foods:
    print(food)
