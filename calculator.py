import math

def square_root():
    try:
        x = float(input("Enter a number: "))
        if x < 0:
            print("Error: Cannot calculate square root of a negative number.")
            return
        print(f"√{x} = {math.sqrt(x)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def factorial():
    try:
        x = int(input("Enter a non-negative integer: "))
        if x < 0:
            print("Error: Factorial is not defined for negative numbers.")
            return
        print(f"{x}! = {math.factorial(x)}")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

def natural_log():
    try:
        x = float(input("Enter a positive number: "))
        if x <= 0:
            print("Error: Natural logarithm is only defined for positive numbers.")
            return
        print(f"ln({x}) = {math.log(x)}")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def power():
    try:
        x = float(input("Enter the base number: "))
        b = float(input("Enter the exponent: "))
        print(f"{x}^{b} = {math.pow(x, b)}")
    except ValueError:
        print("Invalid input! Please enter valid numbers.")

def main():
    while True:
        print("\nScientific Calculator Menu:")
        print("1. Square Root (√x)")
        print("2. Factorial (x!)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power (x^b)")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            square_root()
        elif choice == "2":
            factorial()
        elif choice == "3":
            natural_log()
        elif choice == "4":
            power()
        elif choice == "5":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
