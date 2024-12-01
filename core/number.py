from .validators import NumberValidator

class ArbitraryPrecisionNumber:
    def __init__(self, value, base=10):
        """
        Initialize an arbitrary precision number
        
        Args:
            value (str, int, list): Number representation
            base (int): Numerical base (2-36)
        """
        # Validate base and input
        NumberValidator.validate_base(base)
        NumberValidator.validate_input(value, base)
        
        # Core number attributes
        self.base = base
        self.sign = 1  # 1 for positive, -1 for negative
        self.digits = self._parse_input(value)
    
    def _parse_input(self, value):
        """
        Parse input into internal digit representation
        
        Handles:
        - Strings (decimal, hex, etc.)
        - Integers
        - Lists of digits
        """
        # Handle different input types
        if isinstance(value, int):
            value = str(abs(value))
        
        # Handle sign
        if isinstance(value, str):
            if value.startswith('-'):
                self.sign = -1
                value = value[1:]
        
        # Convert to list of digits (reversed for easier arithmetic)
        if isinstance(value, str):
            return [int(d, self.base) for d in reversed(value.upper())]
        elif isinstance(value, list):
            return value
        else:
            raise ValueError("Unsupported input type")
    
    def __str__(self):
        """String representation of the number"""
        digits_str = ''.join([
            '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[d] 
            for d in reversed(self.digits)
        ])
        return f"{'-' if self.sign == -1 else ''}{digits_str}"

    def __repr__(self):
        return f"ArbitraryPrecisionNumber('{self}', base={self.base})"