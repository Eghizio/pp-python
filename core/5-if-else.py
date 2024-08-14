import random

age = random.randint(1, 100)

print(f"You are {age} years old.")

if age >= 18:
    print("You are an adult!")
elif age >= 11:
    print("You are a teenager")
else:
    print("You are a child")


# Ternary operator
a = 5
b = 7
min = "a is minimum" if a < b else "b is minimum"
print(min)