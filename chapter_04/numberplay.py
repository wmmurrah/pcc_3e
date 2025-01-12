# numberplay.py

# Counting to 20
for value in range(1, 21):
    print(value)

# One million
million = list(range(1, 1000001))    
min(million)
max(million)
sum(million)

odds = list(range(2,21,2))
for value in odds:
    print(value)

threes = list(range(3, 31, 3))
for value in threes:
    print(value)

cubes = [value**3 for value in range(1, 11)]
for cube in cubes:
    print(cube)
