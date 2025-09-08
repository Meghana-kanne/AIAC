def fibonacci(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position in the Fibonacci sequence (0-indexed).

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.

    Example:
        fibonacci(5) -> 5
        fibonacci(0) -> 0
        fibonacci(1) -> 1
    """
    # The Fibonacci sequence is defined as:
    # F(0) = 0
    # F(1) = 1
    # F(n) = F(n-1) + F(n-2) for n > 1

    if n < 0:
        # Negative indices are not allowed in Fibonacci sequence
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        # Base case: the 0th Fibonacci number is 0
        return 0
    elif n == 1:
        # Base case: the 1st Fibonacci number is 1
        return 1
    else:
        # Recursive case: sum of the two preceding Fibonacci numbers
        return fibonacci(n-1) + fibonacci(n-2)

# Example usage and explanation:
if __name__ == "__main__":
    num = int(input("Enter the value of n to find the nth Fibonacci number: "))
    print(f"The {num}th Fibonacci number is: {fibonacci(num)}")

"""
Explanation:
-------------
- The function 'fibonacci' computes the nth Fibonacci number using recursion.
- It checks for base cases (n == 0 and n == 1) and returns the corresponding value.
- For n > 1, it recursively calls itself to compute the (n-1)th and (n-2)th Fibonacci numbers and returns their sum.
- If a negative number is provided, it raises a ValueError.
- The example usage allows the user to input a value for n and prints the corresponding Fibonacci number.
"""
