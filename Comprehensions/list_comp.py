squares = []

for x in range(1, 6):
    squares.append(x ** 2)
print(squares)

squares_comp = [x**2 for x in range(1, 6)]
print(squares_comp)

# Even numbers

even_numbers = [x for x in range(1, 6) if x % 2 == 0]
print(even_numbers)

# With String
letters = [ch.upper() for ch in "hello"]
print(letters)