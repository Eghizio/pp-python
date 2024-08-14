def add(*argv):
    total = 0
    for a in argv:
        total += a
    return total

def minimum(*argv):
    min = float("inf")
    for a in argv:
        if a < min:
            min = a
    return min

def maximum(*argv):
    max = float("-inf")
    for a in argv:
        if a > max:
            max = a
    return max

def multiply(*argv):
    if len(argv) == 0: return 0
    result = 1
    for a in argv:
        result *= a
    return result

print("Add: ", add(2,5,1,4,3))
print("Min: ", minimum(2,5,1,4,3))
print("Max: ", maximum(2,5,1,4,3))
print("Multiply: ", multiply(2,5,1,4,3))

def factorial(x):
    if x <= 1: return 1
    return x * factorial(x-1)

print(factorial(5))