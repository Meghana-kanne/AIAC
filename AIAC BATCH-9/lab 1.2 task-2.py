"""
lab 1.1 -2.py

This script generates and prints the Fibonacci series up to n terms.
"""

def fibonacci_series(n):
    """Generate Fibonacci series up to n terms."""
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print("Fibonacci series up to", n, "terms:")
    print(fibonacci_series(n))