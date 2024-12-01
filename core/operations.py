from .number import ArbitraryPrecisionNumber

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
        # Placeholder for subtraction logic
        raise NotImplementedError("Subtraction not yet implemented")
    
    @classmethod
    def multiply(cls, num1, num2):
        """
        Perform multiplication using grade-school algorithm
        
        Considerations:
        - Handle sign
        - Efficient digit-wise multiplication
        """
        # Ensure same base
        if num1.base != num2.base:
            raise ValueError("Cannot multiply numbers with different bases")
        
        # Determine sign
        result_sign = num1.sign * num2.sign
        
        # Pad digits
        max_len1, max_len2 = len(num1.digits), len(num2.digits)
        result_digits = [0] * (max_len1 + max_len2)
        
        # Multiply each digit
        for i, d1 in enumerate(num1.digits):
            carry = 0
            for j, d2 in enumerate(num2.digits):
                product = d1 * d2 + result_digits[i+j] + carry
                result_digits[i+j] = product % num1.base
                carry = product // num1.base
            
            # Handle final carry
            if carry:
                result_digits[i + max_len2] += carry
        
        # Remove leading zeros
        while result_digits and result_digits[-1] == 0:
            result_digits.pop()
        
        # Create result number
        result = ArbitraryPrecisionNumber(list(reversed(result_digits)), num1.base)
        result.sign = result_sign
        return result