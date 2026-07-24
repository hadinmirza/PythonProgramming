words = ["hi", "hello", "hey", "howdy"]

result = [word.upper() for word in words if len(word) > 3]
print(result)