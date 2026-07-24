total = 0
for i in range(1,101):
    if i % 2 == 0:
        total = total + i

print("Sum using loop:", total)

OneLineComprehension = sum([i for i in range(1, 101) if i % 2 == 0])
print("Sum using list comprehension:", OneLineComprehension)

        
