import math

def calculator():
    """Advanced command-line calculator with arithmetic and trigonometric functions."""
    try:
        print("\nAvailable operations:")
        print(" +  (Addition)   -  (Subtraction)   *  (Multiplication)   /  (Division)")
        print(" ^  (Exponentiation)   %  (Modulus)   √  (Square Root)")
        print(" sin (Sine)   cos (Cosine)   tan (Tangent)")

        operation = input("\nEnter operation: ").strip().lower()

        if operation in ["sin", "cos", "tan", "√"]:
            num = float(input("Enter the number: "))
            if operation == "√":
                if num < 0:
                    print("Error: Square root of a negative number is not allowed!")
                    return
                result = math.sqrt(num)
            elif operation == "sin":
                result = math.sin(math.radians(num))  # Convert degrees to radians
            elif operation == "cos":
                result = math.cos(math.radians(num))
            elif operation == "tan":
                if num % 90 == 0 and (num // 90) % 2 != 0:
                    print("Error: Tangent is undefined at 90° + k*180°")
                    return
                result = math.tan(math.radians(num))
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    return
                result = num1 / num2
            elif operation == "^":
                result = num1 ** num2
            elif operation == "%":
                if num2 == 0:
                    print("Error: Modulus by zero is not allowed!")
                    return
                result = num1 % num2
            else:
                print("Invalid operation! Please choose a valid operation.")
                return

        print(f"\nResult: {result:.6f}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
