## Arbitrary Precision Calculator

### Project Overview

The Arbitrary Precision Calculator is a Python-based computational tool designed to perform arithmetic and scientific operations with numbers of arbitrary size and precision. It supports operations in various bases (from binary to base-36), ensuring accurate calculations without being limited by standard data types. This calculator provides a modular and extensible framework suitable for advanced mathematical computations and is accessible through a command-line interface (REPL).

## Features

### Core Functionality

- ArbitraryPrecisionNumber
- Arbitrary precision integer arithmetic
- Support for multiple numerical bases (2-36)
- Basic operations:

    - Addition
    - Subtraction
    - Multiplication
    - Division
    - Modulo
    - Exponentiation
    - Factorial

### Bonus Features

- Non-decimal base support
- Fraction handling
- Logarithmic operations
- Scientific computational capabilities

## Project Structure
   
```
/arbitrary_precision_calc/
│
├── core/               # Core number representation and operations
│   ├── number.py       # Arbitrary precision number class
│   ├── operations.py   # Mathematical operations
│   └── validators.py   # Input validation
│
├── utils/              # Utility modules
│   ├── base_converter.py   # Base conversion utilities
│   └── exceptions.py   # Custom exceptions
│
├── advanced/           # Advanced mathematical functions
│   ├── scientific.py   # Advanced math operations
│   └── performance.py  # Optimization techniques
│
├── interfaces/         # User interaction
│   └── repl.py         # Interactive calculator interface
│
└── main.py             # Application entry point
```

### Installation:

```
Prerequisites

Python 3.8+
No external libraries required for core functionality

```


## Setup:

```
git clone https://github.com/kihuni/arbitrary_precision_calc.git
cd arbitrary-precision-calculator

```
  
## Usage

### Interactive REPL

```
python main.py

```

## Example Usage:

```
# Create numbers in different bases
num1 = ArbitraryPrecisionNumber("1010", base=2)  # Binary
num2 = ArbitraryPrecisionNumber("FF", base=16)  # Hexadecimal

# Perform operations
result = num1.add(num2)

```

## Advanced Features:

### Base Conversion

```
# Convert between bases
decimal_value = BaseConverter.to_decimal("1010", from_base=2)
hex_value = BaseConverter.from_decimal(decimal_value, to_base=16)

```
  
## Scientific Operations:

```
# Factorial of large numbers
large_factorial = ScientificOperations.factorial(100)

# Efficient exponentiation
power_result = ScientificOperations.power(base=2, exponent=50)

```
## Supported Bases

- Binary (base 2)
- Octal (base 8)
- Decimal (base 10)
- Hexadecimal (base 16)
- Custom bases up to base 36

## Limitations

- Current implementation focuses on integer calculations
- Floating-point precision requires further development
- Some advanced scientific functions are placeholders

If you want to contribute:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

