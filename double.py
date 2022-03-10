def doubler(func):
    def wrapper():
        func()
        func()
    return wrapper
