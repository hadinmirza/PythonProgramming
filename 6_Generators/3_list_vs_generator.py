list_squares = [x ** 2 for x in range(10)]
generator_squares = (x ** 2 for x in range(10))

print(list_squares)
print(generator_squares)

print("\nDifference:")
print("List stores all values in memory.")
print("Generator creates values only when required.")