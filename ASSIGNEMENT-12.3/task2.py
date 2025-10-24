def bubble_sort(arr):
    """
    Sorts a list 'arr' in-place using the bubble sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if elements are out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Example usage:
if __name__ == "__main__":
    nums = [64, 34, 25, 12, 22, 11, 90]
    print("Original list:", nums)
    bubble_sort(nums)
    print("Sorted list:  ", nums)
