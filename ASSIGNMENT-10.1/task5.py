#refoctor the code below to use list comprehension instead of a for loop
import time
start_time=time.time() #record the start time
nums = [i for i in range(1,1000000)] #list of numbers from 1 to 1 million
squares = []
for n in nums:
    squares.append(n**2)
print(len(squares))
end_time=time.time()
print("Time taken:",end_time-start_time)
def factorial(n: int) -> int:
    """Calculate the factorial of a number.

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
