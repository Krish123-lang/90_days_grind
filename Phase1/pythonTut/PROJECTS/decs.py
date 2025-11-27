def my_decorator(func):
    def wrapper():
        print("I will be printed before the main function!")
        func()
    return wrapper

@my_decorator
def say_cheese():
    print("yo ho ho !")

say_cheese()

def logger(func):
    def wrapper():
        print("Function is being called...")
        func()
        print("Function call finished.")
    return wrapper

@logger
def greet():
    print("Hello!")

greet()