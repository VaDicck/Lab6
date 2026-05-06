import sys

def add(a, b):
    sys.stdout.write(f"Adding {a} + {b}\n")
    return a + b

def sub(a, b):
    return round(a - b, 2)

def mul(a, b):
    return a * b

def div(a, b):
    return a / b