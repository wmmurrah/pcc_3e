# conditionals.py

# Conditional tests
sailboat = "precision 23"
print("Is sailboat == 'precision 23'? I predict True")
print(sailboat == "precision 23")

sailboats = ["precision 23", "cape dory 36", "passport 40", "ericson 38"]
lengths_sailboats = [23, 36, 40, 38]
# More conditionals
cat_name = "luke"
boy_name = "Luke"

cat_name == boy_name
cat_name.lower() == boy_name.lower()

sailboat in sailboats
cat_name not in sailboats
boy_name in sailboats

lengths_sailboats[0] > lengths_sailboats[1]


age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, your are to younge to vote.")
    print("Please register to vote as soon as you turn 18!")

# if-elif-else chain
age = 12
if age < 4:
    print("Your admission cost ist $0.")
elif age < 18:
    print("your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 75
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")


# Multiple Conditionals

alien_color = "green"
if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
elif alien_color == "red":
    print("you earned 15 points!")


alien_color = "yellow"
if alien_color == "green":
    points = 5
elif alien_color == "yellow":
    points = 10
elif alien_color == "red":
    points = 15

print(f"You earned {points} points!")

# Stages of life

age = 1
if age < 2:
    stage = "baby"
elif age < 4:
    stage = "toddler"
elif age < 13:
    stage = "kid"
elif age < 20:
    stage = "teenager"
elif age < 65:
    stage = "adult"
else:
    stage = "elder"


print(f"You are in the {stage} stage of life.")

# Favorite Friuts
favorite_fruits = ["apple", "watermelon", "mango", "orange"]

fruits_to_serve = []
if "grapes" in favorite_fruits:
    fruits_to_serve.append("grapes")
if "apple" in favorite_fruits:
    fruits_to_serve.append("apple")
if "kiwi" in favorite_fruits:
    fruits_to_serve.append("kiwi")
if "orange" in favorite_fruits:
    fruits_to_serve.append("orange")
if "mango" in favorite_fruits:
    fruits_to_serve.append("mango")

for fruit in fruits_to_serve:
    print(f"We will be serving {fruit}'s!")
print("Please enjoy!")
