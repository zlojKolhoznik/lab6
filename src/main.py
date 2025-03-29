# Usage: calc <add|subtract|mult|div> <number1> <number2>
# Example: calc add 2 3

import sys
from calculator import Calculator

operations = {
    "add": Calculator.add,
    "subtract": Calculator.subtract,
    "mult": Calculator.multiply,
    "div": Calculator.divide
}


def main():
    if len(sys.argv) != 4:
        print("Usage: calc <add|subtract|mult|div> <number1> <number2>")
        sys.exit(1)

    a = float(sys.argv[2])
    b = float(sys.argv[3])
    if operations.keys().__contains__(sys.argv[1]):
        print(operations[sys.argv[1]](a, b))
    else:
        print("Invalid operation")
    

if __name__ == "__main__":
    main()