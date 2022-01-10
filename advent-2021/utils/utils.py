from functools import wraps
import time

def read_input(path):
    with open(path, 'r') as f:
        file = f.read().splitlines()
    return file

def read_input_whole(path):
    with open(path, 'r') as f:
        file = f.read()
    return file

def timer(function):
    @wraps(function)
    def measure(*args, **kwargs):
        start = time.time()
        try:
            return function(*args, **kwargs)
        finally:
            end = time.time()
            print(f"Total execution time: {end-start:.2f} ms")
    return measure