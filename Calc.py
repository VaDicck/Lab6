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
    
def print_menu():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power")
    
if __name__ == "__main__":
    print_menu()