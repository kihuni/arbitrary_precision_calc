## Arbitrary Precision Calculator

The Arbitrary Precision Calculator is a Python-based computational tool designed to perform arithmetic and scientific operations with numbers of arbitrary size and precision. It supports operations in various bases (from binary to base-36), ensuring accurate calculations without being limited by standard data types. This calculator provides a modular and extensible framework suitable for advanced mathematical computations and is accessible through a command-line interface (REPL).

## Components

1. ArbitraryPrecisionNumber
This class represents numbers with arbitrary precision in a specified base. It handles initialization, validation, and parsing of input values.

## Key Features:

Supports integers, strings, and lists as input.
Works with bases from 2 to 36.
Internally represents numbers as a list of digits in reverse order for efficient arithmetic.
Example Usage:

```
num = ArbitraryPrecisionNumber("101", base=2)  # Represents binary 101 (5 in decimal)

```

2. NumberOperations
   
This class implements core arithmetic operations (addition and multiplication) for arbitrary precision numbers.

## Key Features:

- Ensures compatibility across bases.
- Handles carry/borrow operations for addition.
- Supports future extensibility for subtraction and division.
  
## Example Usage:

- num1 = ArbitraryPrecisionNumber("101", base=2)
- num2 = ArbitraryPrecisionNumber("11", base=2)
- result = NumberOperations.add(num1, num2)  # Binary addition: 101 + 11 = 1000
  
1. BaseConverter
   
This utility class provides methods for converting numbers between bases.

## Key Methods:

- to_decimal: Converts a number from any base to decimal.
- from_decimal: Converts a decimal number to any base.

## Example Usage:

- decimal = BaseConverter.to_decimal("101", from_base=2)  # Converts binary to decimal (5)
- binary = BaseConverter.from_decimal(5, to_base=2)  # Converts decimal to binary ("101")
  
1. ScientificOperations
   
Implements advanced mathematical functions like power and factorial for arbitrary precision numbers.

## Key Features:

- Efficient binary exponentiation.
- Factorial computation for very large numbers.
  
## Example Usage:

```
result = ScientificOperations.power(ArbitraryPrecisionNumber("2"), 10)  # 2^10 = 1024
factorial_result = ScientificOperations.factorial(100)  # Computes 100!

```
1. CalculatorREPL
   
Provides an interactive command-line interface for the calculator.

## Key Features:

- Accepts mathematical expressions as input.
- Handles errors gracefully.
- Offers exit commands for user convenience.
  
## Example Usage:


>>> 2 ^ 10
1024
>>> 100!
93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
>>> exit

1. ArbitraryPrecisionCalculator
   
The central class orchestrates operations and manages input preprocessing and evaluation.

## Key Features:

- Supports basic and scientific computations.
- Parses and evaluates mathematical expressions securely.
- Modular design for extensibility.
- Example Usage:


```
calculator = ArbitraryPrecisionCalculator()
result = calculator.evaluate("2 ^ 10 + 50!")

```

Code Execution
```
Run the program using the command-line interface:

python main.py

```
This starts the REPL where users can perform calculations interactively.

## Extensibility

This calculator is built with a modular architecture, allowing seamless addition of:

## New mathematical operations.

- Support for additional bases.
- Integration with external libraries for enhanced functionality.
  
With its robust design, the Arbitrary Precision Calculator serves as a reliable tool for both basic arithmetic and advanced computations.