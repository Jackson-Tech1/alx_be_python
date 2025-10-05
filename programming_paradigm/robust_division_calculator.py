def safe_divide(numerator, denominator):
    """
    Safely divide two numbers with error handling.
    
    Args:
        numerator (str/float): Numerator
        denominator (str/float): Denominator
    
    Returns:
        str: Result or error message
    """
    # Convert to floats
    try:
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    # Perform division
    try:
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
