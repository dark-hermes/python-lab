def add(x, y):
    """Add two numbers.

    Args:
        x (int): First number.
        y (int): Second number.

    Returns:
        int: Sum of x and y.
        
    >>> add(1, 2)
    3
    >>> add(2, 2)
    4
    """
    return x + y


def subtract(x, y):
    """Subtract two numbers.
    
    Args:
        x (int): First number.
        y (int): Second number.
        
    Returns:
        int: Difference of x and y.
        
    >>> subtract(2, 1)
    1
    >>> subtract(2, 2)
    0
    """
    return x - y


def multiply(x, y):
    """
    Multiply two numbers.
    
    Args:
        x (int): First number.
        y (int): Second number.
        
    Returns:
        int: Product of x and y.
        
    >>> multiply(2, 2)
    4
    >>> multiply(2, 0)
    0
    """
    return x * y


def divide(x, y):
    """
    Divide two numbers.
    
    Args:
        x (int): First number.
        y (int): Second number.
        
    Returns:
        float: Quotient of x and y.
        
    >>> divide(2, 2)
    1.0
    >>> divide(2, 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: Division by zero is not allowed.
    """
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return x / y