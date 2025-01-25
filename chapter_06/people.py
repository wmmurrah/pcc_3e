# person.py

jhall = {
    'first_name': 'josh',
    'last_name': 'hall',
    'age': 40,
    'city': 'cooksville',
    }

jmurrah = {
    'first_name': 'josh',
    'last_name': 'murrah',
    'age': 49,
    'city': 'chattanooga',
}

rmurrah = {
    'first_name': 'rosalind',
    'last_name': 'murrah',
    'age': 8,
    'city': 'auburn',
}

people = [jhall, jmurrah, rmurrah]

for person in people:
    print(f"\nName: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\nAge: {person['age']}")
    print(f"\nCity: {person['city'].title()}\n\n")






