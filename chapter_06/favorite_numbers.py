# Favorite numbers
favorite_numbers = {
    "hank": 17,
    "katie": 4,
    "rosalind": 4,
    "penny": 8,
    "benny": 1,
}
keys = favorite_numbers.keys()

for key in keys:
    print(f"{key.title()}'s favorite number is {favorite_numbers[key]}.")
