def add(a, b):
    print(f"Adding {a} + {b}")   # конфликтная строка (версия main)
    return a + b

def sub(a, b):
    print(f"Subtracting {b} from {a}")
    result = a - b
    print(f"Result: {result}")
    return result

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b
    
def power(a, b):
    return a ** b