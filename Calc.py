import math
def sqrt(a):
    return math.sqrt(a)

def add(a, b):
    import logging
    logging.info(f"Adding {a} + {b}")  # конфликт
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        print("Division by zero is not allowed, returning None")
        return None
    return a / b