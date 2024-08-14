from time import sleep

msg = "Hi"


print(range(10))

print("\nFor Loop in range:")
for i in range(10):
    print(f"[{i}] {msg}") # Indentacja za pomocą Tab


print("\nFor Loop in range with step:")
for i in range(0, 10, 2):
    print(f"[{i}] {msg}")

print("\nFor Loop in range with negative step:")
for i in range(10, 0, -1):
    print(f"[{i}] {msg}")



level = 1

print("\nWhile Loop:")
while level <= 10:
    print(f"Tring to beat level {level}")
    # sleep(level) # pause for X seconds
    print(f"Finished level {level}! Level up!")
    level = level + 1


print("\nWhile Loop with Break statement:")
while level <= 100:
    print(f"Tring to beat level {level}")
    # sleep(1) # pause for X seconds
    print(f"Finished level {level}! Level up!")
    level = level + 1

    if level == 21:
        print(f"Done with leveling for today. Level {level} is satisfying for me :)")
        break


print("\nInfinite While Loop with Break:")
while True:
    print(f"Tring to beat level {level}")
    sleep(0.2) # pause for X seconds
    print(f"Finished level {level}! Level up!")
    level = level + 1

    if level == 42:
        break


print("\nInfinite While Loop with Continue and Break:")
while True:
    print(f"Tring to beat level {level}")
    sleep(0.2) # pause for X seconds
    print(f"Finished level {level}! Level up!")
    level = level + 1
    
    if level < 90:
        continue

    print(f"Only couple levels left to 100...")
    if level == 100:
        break
