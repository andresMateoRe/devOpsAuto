# main.py
from prueba import add, subtract, multiply, divide

def is_number(value):
    """Check if the input value is a valid number."""
    try:
        float(value)  # Try converting to float
        return True
    except ValueError:
        return False

def main():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = input("Enter first number: ")
        num2 = input("Enter second number: ")

        # Validate inputs
        if not is_number(num1) or not is_number(num2):
            print("Invalid input. Please enter numeric values.")
            return

        num1 = float(num1)
        num2 = float(num2)

        try:
            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")adsas
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")

        except ValueError as ve:
            print(f"Error: {ve}")  # Catches division by zero
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()
