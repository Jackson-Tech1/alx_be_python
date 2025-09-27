def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.

    Parameters:
    num1 (float): The first number
    num2 (float): The second number
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide')

    Returns:
    float or str: Result of the operation, or error message for division by zero
    """
    operation = operation.strip().lower()
    
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
