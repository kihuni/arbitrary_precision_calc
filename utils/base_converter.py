class BaseConverter:
    @staticmethod
    def to_decimal(number, from_base):
        """
        Convert number from any base to decimal
        
        Args:
            number (str): Number to convert
            from_base (int): Source base
        
        Returns:
            int: Decimal representation
        """
        # Remove any sign
        is_negative = number.startswith('-')
        if is_negative:
            number = number[1:]
        
        # Convert to decimal
        decimal_value = 0
        for i, digit in enumerate(reversed(number.upper())):
            # Convert character to integer value
            digit_value = int(digit, from_base)
            decimal_value += digit_value * (from_base ** i)
        
        return -decimal_value if is_negative else decimal_value
    
    @staticmethod
    def from_decimal(decimal_num, to_base):
        """
        Convert decimal number to specified base
        
        Args:
            decimal_num (int): Number in decimal
            to_base (int): Target base
        
        Returns:
            str: Number in target base
        """
        # Handle sign
        is_negative = decimal_num < 0
        decimal_num = abs(decimal_num)
        
        # Handle zero as a special case
        if decimal_num == 0:
            return '0'
        
        # Conversion algorithm
        digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        converted_digits = []
        
        while decimal_num > 0:
            converted_digits.append(digits[decimal_num % to_base])
            decimal_num //= to_base
        
        # Reconstruct the number with sign
        result = ''.join(reversed(converted_digits))
        return f'-{result}' if is_negative else result