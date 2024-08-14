# Importing from Module
from _utils import print_title


# Zmienne
name = "Pan Kuba"
skill = 9000 + 1
favourite_number = 42
# Zmiana wartości - nadpisanie zmiennej.
favourite_number = 1337

message = f"\nCześć {name}. Mója ulubiona liczba to {favourite_number}"

print(message)



# Math operators
print_title("Math Operators")
print("2 + 2:", 2 + 2 )
print("2 - 2:", 2 - 2 )
print("2 * 2:", 2 * 2 )
print("2 / 2:", 2 / 2 )
print("10 % 3:", 10 % 3 )


# Incrementation and Decrementation
print_title("Incrementation and Decrementation")
number = 10

number += 2
print("+=", number)

number -= 3
print("-=", number)

number *= 4
print("*=", number)

number /= 4
print("/=", number)

number %= 6
print("%=", number)



# Logical operators

print_title("Logical operators")

# Negation
print("not true:", not True )

# Equals and Not Equals
print_title("Comparison operators")
print("2 == 2:", 2 == 2 )
print("2 is 2:",  2 is 2 )

print("2 != 2:",  2 != 2 )
print("2 is not 2:",  2 is not 2 )


# AND operator &&
print_title("AND operator")
print("1 and 1:", True and True )
print("1 and 0:",  True and False )
print("0 and 1:",  False and True )
print("0 and 0:",  False and False )


# OR operator ||
print_title("OR operator")
print("1 or 1 =", True or True )
print("1 or 0 =",  True or False )
print("0 or 1 =",  False or True )
print("0 or 0 =",  False or False )
