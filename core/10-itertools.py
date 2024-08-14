# https://docs.python.org/3/library/itertools.html
import itertools
import operator
from _utils import print_title



print_title("itertools.count()")

iterator = iter([1, 2, 3, 4, 5])

for x in range(10):
    try:
        print(next(iterator))
    except StopIteration:
        print("Iterator ended! Breaking.")
        break



print_title("itertools.count()")
for i in itertools.count(4, 2):
    print(i)
    if i == 16: break



print_title("itertools.cycle() List")
cycle_iterator = itertools.cycle([1, 2, 3, 4, 5])
for i in range(12):
    print(next(cycle_iterator))

print_title("itertools.cycle() String")
cycle_iterator_text = itertools.cycle("ALA")
for i in range(12):
    print(next(cycle_iterator_text))



print_title("itertools.accumulate()")
numbers = [1, 2, 3, 4, 5]
sum = list(itertools.accumulate(numbers))
print("Sum:", sum)

multiplication = list(itertools.accumulate(numbers, func=operator.mul))
print("Multiplication:", multiplication)

numbers = [1, 2, 3, 4, 5]
sum_from_100 = list(itertools.accumulate(numbers, initial=100))
print("Sum with 100:", sum_from_100)



print_title("itertools.chain()")
first = ("a", "b", "c")
second = (1, 2, 3)

for element in itertools.chain(first, second):
    print(element)



print_title("itertools.compress()")
data = ["h", "b", "e", "o", "b", "p"]
mask = [0, 1, 0, 1, 1, 0]
result = itertools.compress(data, mask)
print(list(result))



print_title("itertools.product()")
FACE_CARDS = ("J", "Q", "K", "A")
SUITS = ("♥", "♦", "♣", "♠")
 
DECK = list(
    itertools.product(
        itertools.chain(range(2, 11), FACE_CARDS),
        SUITS,
    )
)
 
for card in DECK:
    print("{:>2}{}".format(*card), end=" ")
    if card[1] == SUITS[-1]:
        print()
