def factorial_febo(n):
    # Calculate factorial
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i

    # Generate Fibonacci series up to n terms
    fibo = []
    a, b = 0, 1
    for _ in range(n):
        fibo.append(a)
        a, b = b, a + b

    return factorial, fibo

# Example usage:
n = int(input("Enter a number: "))
fact, fib_series = factorial_febo(n)
print(f"Factorial of {n}: {fact}")
print(f"Fibonacci series up to {n} terms: {fib_series}")