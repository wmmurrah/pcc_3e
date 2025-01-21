# Glossary

glossary = {
    "integer": "a whole number (without fractional or decimal components) that can be positive, negative, or zero",
    "float": "a number with a fractional or decimal component",
    "string": "a sequence of characters (such as letters, digits, and symbols) typically used to represent text in a program",
    "boolean": "a data type that represents a logical value—typically either true or false",
    "conditional": "a construct that allows a program to perform different actions depending on whether a certain condition is true or false",
    "List": "An ordered, mutable collection of items",
    "Dictionary": "An unordered, mutable collection of key-value pairs",
    "Tuple": "An ordered, immutable collection of items",
}

keys = glossary.keys()

for key in keys:
    print(f"A {key} is {glossary[key]}.\n")


for key in keys:
    print(f"{key.title()}:\n    {glossary[key].capitalize()}. \n")


for key, value in glossary.items():
    print(f"{key.title()}:\n    {value.capitalize()}. \n")

