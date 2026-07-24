numbers = [10, 20, 30, 40]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break