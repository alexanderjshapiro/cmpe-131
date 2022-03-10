import time


def calculate_time(func):
    def wrapper():
        start = time.time()
        func()
        duration = time.time() - start
        print("Total time " + str(duration))
    return wrapper
