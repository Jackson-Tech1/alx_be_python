def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    num1 (float): First number
    num2 (float): Second number
    operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    float or str: Result of operation or an error message if invalid
    """
    operation = operation.strip().lower()  # Normalize input

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if
