guests = ["Albert Einstein", "Herbert Simon", 
          "Rosalind Franklin"]

# Guest list
for guest in guests:
    print(f"Dear {guest}, I invite you for a titilating dinner.")

# Changing guest list
print(f"It turns out that {guests[0]} can't make the dinner.")

guests[0] = "Richard Feynman"

print(guests)

for guest in guests:
    print(f"Dear {guest}, please join me for dinner.")

# More guersts
print("Dear dinner guests, I found a bigger table"
       "so I am invitng more people.")

guests.insert(0, "John Holland")
guests.insert(2, "Paul Meehl")
guests.append("Allen Newell")
print(guests)
len(guests)

for guest in guests:
    print(f"Dear {guest}, Please join us for dinner.")


# Shrinking guest list

print("Dinner guests, unfortunately, I can now only"
      "invite two dinner guests. ")   

while len(guests) > 2:
    uninvited = guests.pop()
    print(f"Dear {uninvited}, I am sorry to inform you "
          "that I am unable to have you over for dinner "
          "as previously scheduled.") 
    
    
print(guests)

del guests[0:2]

print(guests)

len(guests)