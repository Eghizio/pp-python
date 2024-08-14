# Function definition
def do_something():
    print("Doing something!")

do_something()



# Pass keyword
def do_nothing(): pass

do_nothing()



# Argument/Parameter
def print_message(msg):
    print("[MESSAGE]:" + msg)

print_message("Hello there!")



# Multiple arguments/parameters
def add(x, y):
    print(x + y)

add(2, 2)

result = add(2, 2)
print(result)



# Default argument value
def power(a, x = 2):
    print(a ** x)

power(5)
power(5, 3)



# Return keyword
def multiply(a, b):
    return a * b

multiply(2, 3)
result = multiply(2, 4)
print(result)
print( multiply(3, 5) )



# Named/Keyword arguments
def send_to(msg, name):
    print(f"[{name}]: {msg}")

send_to(name="Adam", msg = "Hello there")



# Unlimited arguments - *args
def some_function(*argv):
    for arg in argv:
        print(arg)


some_function("first", 2, "c", None)


# Keyword Arguments
def function_with_keyword_arguments(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} == {value}")

function_with_keyword_arguments(foo="A", bar="b", baz="c")



# Returning multiple values
def min_max(*args):
    minimum = min(args)
    maximum = max(args)
    return minimum, maximum

lowest, highest = min_max(42, 12, 51, 72)
print(lowest, highest)
