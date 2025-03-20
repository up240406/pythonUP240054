# Level 1

# 1. Iterate 0 to 10 using for loop and while loop
for i in range(11):
    print(i)

print("---")

j = 0
while j <= 10:
    print(j)
    j += 1

print("---")

# 2. Iterate 10 to 0 using for loop and while loop
for i in range(10, -1, -1):
    print(i)

print("---")

j = 10
while j >= 0:
    print(j)
    j -= 1

print("---")

# 3. Print a triangle
for i in range(1, 8):
    print("#" * i)

print("---")

# 4. Nested loop to create 8x8 grid pattern
for i in range(8):
    print("# " * 8)

print("---")

# 5. Multiplication table pattern
for i in range(11):
    print(f"{i} x {i} = {i * i}")

print("---")

# 6. Iterate through a list and print items
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

print("---")

# 7. Print even numbers from 0 to 100
for i in range(0, 101, 2):
    print(i, end=' ')

print("\n---")

# 8. Print odd numbers from 0 to 100
for i in range(1, 101, 2):
    print(i, end=' ')

print("\n---")


