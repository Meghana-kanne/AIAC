def calculate_sum(numbers):
    return sum(numbers)

if __name__ == "__main__":
    nums = input("Enter numbers separated by spaces: ")
    num_list = [float(num) for num in nums.split()]
    total = calculate_sum(num_list)
    print(f"The sum of the numbers is: {total}")