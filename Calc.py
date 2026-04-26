def add(a, b):
    print(f"Adding {a} + {b}")   # конфликтная строка (версия main)
    return a + b

def sub(a, b):
    print(f"Subtracting {a} - {b}")   # конфликтная строка (версия main)
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return a
    return a / b
    
def power(a, b):
    return a ** b
    
def printHelp():
    print("help")
    
def print_version():
    print("Calc v1.0")