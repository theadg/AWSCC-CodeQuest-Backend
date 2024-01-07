import time

def timing_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        result = original_function(*args, **kwargs)
        return result + 5;
    return wrapper_function

@timing_decorator
def plusFive(num1):
    return num1 + 5;

print(plusFive(1))  # Output: slow_function ran in 2.002163887023926 seconds