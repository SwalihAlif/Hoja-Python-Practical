numbers = [1,2,3,4,5,6,2,3,4]

unique_numbers = {x**2 for x in numbers}

print(unique_numbers)

even_set = {x for x in numbers if x % 2 == 0}
print(even_set)