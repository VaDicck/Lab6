def add(a, b):
    import logging
    logging.info(f"Adding {a} + {b}")  # конфликт
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b