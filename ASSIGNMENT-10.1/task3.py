def calculate_percentage(base_value: float, percentage: float) -> float:
    """Calculate the percentage of a given base value.

    Args:
        base_value (float): The value to calculate the percentage from.
        percentage (float): The percentage to apply.

    Returns:
        float: The result of base_value * percentage / 100.
    """
    return base_value * percentage / 100

# Define the base value and percentage
base_amount = 200
discount_rate = 15

# Calculate and print the result
result = calculate_percentage(base_amount, discount_rate)
print(result)