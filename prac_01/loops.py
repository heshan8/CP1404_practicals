
"""
3. Creating different loops
"""

for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')
print()

for i in range(20, 1, -1):
    print(i, end=' ')
print()

star_count = int(input("Stars: "))
for stars in range(star_count):
    print("*", end="")
print()

star_count = int(input("Stars: "))
for i in range(1, star_count + 1):
    print("*" * i)
print()
