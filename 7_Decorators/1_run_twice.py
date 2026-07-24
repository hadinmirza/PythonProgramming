def run_twice(func):
    func()
    func()

def say_hi():
    print("hi")
    
run_twice(say_hi)