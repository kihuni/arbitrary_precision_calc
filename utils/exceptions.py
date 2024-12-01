class ArbitraryPrecisionError(Exception):
    """Base exception for Arbitrary Precision Calculator"""
    pass

class BaseConversionError(ArbitraryPrecisionError):
    """Exception raised for base conversion errors"""
    pass

class OperationError(ArbitraryPrecisionError):
    """Exception raised for mathematical operation errors"""
    pass