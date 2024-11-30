from core.number import ArbitraryPrecisionNumber

class NumberOperations:
    @classmethod
    def add(cls, num1, num2):
        """
        Perform addition of two arbitrary precision numbers
        
        Key considerations:
        - Handle different signs
        - Manage carry
        - Preserve base
        """
        # Ensure same base
        if num1.base != num2.base:
            raise ValueError("Cannot add numbers with different bases")
        
        # Handle sign differences
        if num1.sign != num2.sign:
            return cls._handle_mixed_sign_addition(num1, num2)
        
        # Pad digits to equal length
        max_len = max(len(num1.digits), len(num2.digits))
        digits1 = num1.digits + [0] * (max_len - len(num1.digits))
        digits2 = num2.digits + [0] * (max_len - len(num2.digits))
        
        # Perform addition
        result_digits = []
        carry = 0
        for d1, d2 in zip(digits1, digits2):
            total = d1 + d2 + carry
            result_digits.append(total % num1.base)
            carry = total // num1.base
        
        if carry:
            result_digits.append(carry)
        
        # Create new number with result
        result = ArbitraryPrecisionNumber(list(reversed(result_digits)), num1.base)
        result.sign = num1.sign
        return result
    
    @classmethod
    def _handle_mixed_sign_addition(cls, num1, num2):
        """
        Handle addition when numbers have different signs
        
        Delegate to subtraction based on absolute values
        """
        # Logic for mixed-sign addition
        pass  # Implement detailed subtraction logic
    
    @classmethod
    def multiply(cls, num1, num2):
        """
        Perform multiplication using grade-school algorithm
        
        Considerations:
        - Handle sign
        - Efficient digit-wise multiplication
        """
        # Implement multiplication logic
        pass