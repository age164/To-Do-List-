"""Simple command-line calculator."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def get_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number.")


def main() -> None:
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    left = get_number("Enter the first number: ")
    op = input("Enter operation (+, -, *, /): ").strip()
    right = get_number("Enter the second number: ")

    if op == "+":
        result = add(left, right)
    elif op == "-":
        result = subtract(left, right)
    elif op == "*":
        result = multiply(left, right)
    elif op == "/":
        result = divide(left, right)
    else:
        raise ValueError("Unsupported operation.")

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
