# numbers.py
for value in range(1, 6):
    print(value)

for value in range(6):
    print(value)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)    

# more concise
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)    

digits = list(range(1, 10))
digits.append(0)
print(digits)

min(digits)
max(digits)
sum(digits)

# List comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)




