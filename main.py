# main.py
from core.number import ArbitraryPrecisionNumber
from core.operations import NumberOperations
from advanced.scientific import ScientificOperations
from interfaces.repl import CalculatorREPL
import re

class ArbitraryPrecisionCalculator:
    def __init__(self):
        # Dependency injection for modularity
        self.number_class = ArbitraryPrecisionNumber
        self.operations = NumberOperations
        self.scientific = ScientificOperations
    
    def evaluate(self, expression):
        """
        Central method to parse and compute expressions
        
        Supports:
        - Basic arithmetic
        - Scientific operations
        - Multi-base calculations
        """
        try:
            # Preprocessing
            expression = self._preprocess_expression(expression)
            
            # Parsing and computation logic
            result = self._compute_expression(expression)
            
            return str(result)
        except Exception as e:
            return f"Calculation Error: {e}"
    
    def _preprocess_expression(self, expression):
        """
        Prepare expression for computation
        
        - Base prefix parsing
        - Factorial handling
        - Power notation
        """
        # Base prefix handling (e.g., 0b1010, 0x1A)
        expression = expression.replace('0b', 'ArbitraryPrecisionNumber("', 1) \
                                  .replace('0x', 'ArbitraryPrecisionNumber("', 1)
        
        # Base suffixes
        def base_replacer(match):
            num, base = match.group(1), match.group(2)
            return f'ArbitraryPrecisionNumber("{num}", {base})'
        
        expression = re.sub(r'(\d+)_(\d+)', base_replacer, expression)
        
        # Factorial handling
        def factorial_replacer(match):
            return f'ScientificOperations.factorial(ArbitraryPrecisionNumber("{match.group(1)}"))'
        
        expression = re.sub(r'(\d+)!', factorial_replacer, expression)
        
        # Power and log handling
        expression = expression.replace('^', '**')
        expression = expression.replace('log(', 'ScientificOperations.logarithm(')
        
        return expression
    
    def _compute_expression(self, expression):
        """
        Core computational method
        
        Uses eval with restricted environment
        """
        # Secure evaluation with limited context
        result = eval(
            expression, 
            {"__builtins__": None}, 
            {
                "ArbitraryPrecisionNumber": self.number_class,
                "ScientificOperations": self.scientific,
                "pow": self.scientific.power,
                "abs": abs
            }
        )
        
        return result

def main():
    """
    Entry point for the Arbitrary Precision Calculator
    
    Initializes the calculator and starts the REPL interface
    """
    calculator = ArbitraryPrecisionCalculator()
    repl = CalculatorREPL(calculator)
    repl.run()

if __name__ == "__main__":
    main()
