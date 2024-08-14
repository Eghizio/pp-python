from _utils import print_title

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]


print("\nMy numbers as a list:\n", numbers)


# Comparing Lists
print("\nComparing Lists:\n")
print("Same lists (equals)?:", numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Same lists (is)?:", numbers is [1, 2, 3, 4, 5, 6, 7, 8, 9])


# Adding elements
print("\nAdding a number:\n")
numbers.append(10)
print(numbers)


# Looping over the elements
print("\nHere are my numbers:\n")
for num in numbers:
    print(num)



# List length
amount_of_numbers = len(numbers)
print("\nPrinting the length of the list (amount of elements):\n", amount_of_numbers)


# Accessing elements via Index
print("\nPrinting the first element of the list:\n", numbers[0])

print("\nPrinting the last element of the list:\n", numbers[len(numbers) - 1])
print("\nPrinting the last element of the list:\n", numbers[amount_of_numbers - 1])
print("\nPrinting the last element of the list:\n", numbers[-1])


# Reassigning value based on Index
numbers[-1] = 0
print("\nModyfing last element:\n", numbers)



# Ooopsie
# print("\nAccesing elements out of boundaries:\n", print(numbers[100]))


# Try/Except & Raising custom Errors
try:
    raise Exception("Custom Error/Exception message.")
except:
    print("\nWe caught our error and program continues :)\n")



# Try/Except block - catching/handling errors
try:
    print(numbers[100])
except IndexError:
    print("\nWe got out Index out of boundaries!\n")
except:
    print("\nThere was another Error.\n")
else:
    print("\nNothing went wrong :)\n")
finally:
    print("Try block finished!")



# Enumerating with Index
print_title("Enumerating with Index")
for i, val in enumerate(numbers):
    print(f"[{i}]: {val}")



# Looping over two Lists at the same time
print_title("Zipping two Lists")
first_names = ["Adam", "Beth", "Cecil"]
last_names = ["Danone", "Erricson", "Ford", "Tesla"]

for first, last in zip(first_names, last_names):
    full_name = f"{first} {last}"
    print(full_name)



# List comprehension - create another List based on Loop
numbers_copy = [x for x in numbers]

print("\nList comprehension:\n", numbers_copy)



# List comprehension - create modified List based on Loop
doubled = [x * 2 for x in numbers]

print("\nList comprehension with Mapping:\n", doubled)


# List comprehension - create modified List based on Loop & Condition
threes = [x for x in numbers if x == 3]

print("\nList comprehension with Conditional Filtering:\n", threes)


# List comprehension - create modified List based on Loop & If/Else Condition
everything_doubled_but_threes = [x if x == 3 else x * 2 for x in numbers]

print("\nList comprehension with Conditional Mapping:\n", everything_doubled_but_threes)


# Destructuring - unpacking values from List into Variables
students = ["Adam", "Beth", "Cecil"]

print("\nDestructuring list into single elements")
adam, beth, cecil = students
print(adam, beth, cecil)
