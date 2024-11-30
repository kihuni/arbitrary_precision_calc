class ArbitraryPrecisionNumber:
    def __init__(self, value, base=10):
        """
        Initialize an arbitrary precision number
        
        Args:
            value (str, int, list): Number representation
            base (int): Numerical base (2-36)
        """
        # Validate base and input
        self._validate_base(base)
        self._validate_input(value, base)
        
        # Core number attributes
        self.base = base
        self.sign = 1  # 1 for positive, -1 for negative
        self.digits = self._parse_input(value)
    
    def _validate_base(self, base):
        """Validate the numerical base"""
        if base < 2 or base > 36:
            raise ValueError(f"Base must be between 2 and 36, got {base}")
    
    def _validate_input(self, value, base):
        """
        Comprehensive input validation
        - Check input type
        - Validate characters for given base
        """
        # Support different input types
        if isinstance(value, (int, float)):
            return
        
        if isinstance(value, str):
            # Remove sign for validation
            cleaned_value = value.lstrip('-')
            
            # Define valid characters based on base
            valid_chars = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base])
            
            # Validate each character
            if not all(char.upper() in valid_chars for char in cleaned_value):
                raise ValueError(f"Invalid characters for base {base}")
    
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
            return [int(d) for d in reversed(value)]
        elif isinstance(value, list):
            return value
        else:
            raise ValueError("Unsupported input type")
