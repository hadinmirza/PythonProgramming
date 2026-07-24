def my_max(numbers):
    largest = numbers[0]
    for i in numbers:
        if i > largest:
            largest = i
    return largest

numbers = [10, 40, 70, 80, 30]
print("Largest number:", my_max(numbers))