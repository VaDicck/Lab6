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
    while True:
        print_menu()
        choice = input("Выберите операцию (1-5) или 'q' для выхода: ")
        if choice == 'q':
            break
        if choice not in ('1', '2', '3', '4', '5'):
            print("Неверный ввод, попробуйте снова.")
            continue

        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: нужно вводить числа.")
            continue

        if choice == '1':
            print("Результат:", add(a, b))
        elif choice == '2':
            print("Результат:", sub(a, b))
        elif choice == '3':
            print("Результат:", mul(a, b))
        elif choice == '4':
            res = div(a, b)
            print("Результат:", res)
        elif choice == '5':
            print("Результат:", power(a, b))