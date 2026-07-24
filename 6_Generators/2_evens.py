def evens():
    n = 0
    while True:
        yield n
        n += 2
        
generator = evens()

for i in range(5):
    print(next(generator))