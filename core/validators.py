class NumberValidator:
    @staticmethod
    def validate_base(base):
        """Validate the numerical base"""
        if base < 2 or base > 36:
            raise ValueError(f"Base must be between 2 and 36, got {base}")
    
    @staticmethod
    def validate_input(value, base):
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