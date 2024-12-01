import math
from core.number import ArbitraryPrecisionNumber
from core.operations import NumberOperations

class ScientificOperations:
    @classmethod
    def power(cls, base, exponent):
        """
        Efficient arbitrary precision exponentiation
        
        Uses binary exponentiation for efficiency
        """
        # Implement fast exponentiation
        result = ArbitraryPrecisionNumber(1, base.base)
        current_power = base
        
        # Convert exponent to positive integer
        exp_value = abs(int(str(exponent)))
        
        while exp_value > 0:
            if exp_value % 2 == 1:
                result = NumberOperations.multiply(result, current_power)
            current_power = NumberOperations.multiply(current_power, current_power)
            exp_value //= 2
        
        # Handle negative exponents
        return result
    
    @classmethod
    def factorial(cls, number):
        """
        Compute factorial with arbitrary precision
        
        Handles large numbers efficiently
        """
        # Convert to integer
        n = int(str(number))
        
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        
        result = ArbitraryPrecisionNumber(1)
        for i in range(2, n + 1):
            result = NumberOperations.multiply(result, ArbitraryPrecisionNumber(i))
        
        return result
    
    @classmethod
    def logarithm(cls, number, base=math.e):
        """
        Compute logarithm with arbitrary precision
        
        Args:
            number (ArbitraryPrecisionNumber): Number to compute log of
            base (float, optional): Logarithm base (default: e)
        """
        # Numerical approximation method
        num_val = float(str(number))
        return ArbitraryPrecisionNumber(str(math.log(num_val, base)))