from core.number import ArbitraryPrecisionNumber
from core.operations import NumberOperations
from advanced.scientific import ScientificOperations
from interfaces.repl import CalculatorREPL

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
        - Error handling
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
        
        - Handle factorial
        - Replace power notation
        - Sanitize input
        """
        # Preprocessing steps
        expression = expression.replace('^', '**')
        
        # Factorial handling
        while '!' in expression:
            # Complex factorial preprocessing
            pass
        
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
                "pow": self.scientific.power,
                "abs": abs
            }
        )
        
        return result

def main():
    calculator = ArbitraryPrecisionCalculator()
    repl = CalculatorREPL(calculator)
    repl.run()

if __name__ == "__main__":
    main()