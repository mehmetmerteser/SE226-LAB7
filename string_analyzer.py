
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Error: Division by zero."

def power(x, y):
    return x ** y

def mod(x, y):
    return x % y

if __name__ == "__main__":

    print("Add:", add(2, 3))
    print("Divide by zero test:", divide(10, 0))
